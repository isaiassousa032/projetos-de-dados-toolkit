"""Valida documentação local e originais sem modificar arquivos ou acessar rede."""

from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[2]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def prose(text, strip_inline=True):
    """Retira blocos e trechos de código, preservando números de linhas."""
    result = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            result.append("")
        elif fence is not None:
            result.append("")
        else:
            result.append(re.sub(r"`+[^`]*`+", "", line) if strip_inline else line)
    return "\n".join(result)


def anchors(text):
    counts = defaultdict(int)
    result = set()
    # Mantém o texto dos títulos, incluindo identificadores entre crases.
    for line in prose(text, strip_inline=False).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", match.group(1)).replace("`", "").lower()
        slug = re.sub(r"[^\w\-\s]", "", title, flags=re.UNICODE)
        slug = re.sub(r"\s", "-", slug)
        suffix = "" if counts[slug] == 0 else "-" + str(counts[slug])
        result.add(slug + suffix)
        counts[slug] += 1
    return result


def exact_case(path):
    """Confere capitalização para compatibilidade com GitHub/Linux."""
    if not path.is_relative_to(ROOT):
        return False
    current = ROOT
    for part in path.relative_to(ROOT).parts:
        if part not in {entry.name for entry in current.iterdir()}:
            return False
        current = current / part
    return True


def main():
    errors = []
    nested_git = [p for p in ROOT.rglob(".git") if p != ROOT / ".git"]
    errors.extend("Repositório Git embutido: " + p.relative_to(ROOT).as_posix() for p in nested_git)
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts)
    texts = {p: p.read_text(encoding="utf-8-sig") for p in files if p.suffix == ".md"}
    local_links = 0
    for path, body in texts.items():
        content = prose(body)
        for match in re.finditer(r"!?\[[^\]\n]*\]\(([^\n]*?)\)", content):
            raw = match.group(1).strip()
            target = raw[1:raw.index(">")] if raw.startswith("<") and ">" in raw else raw.split()[0] if raw else ""
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            local_links += 1
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            line = content[:match.start()].count("\n") + 1
            label = f"{path.relative_to(ROOT).as_posix()}:{line}: {target}"
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append("Link ausente/fora da biblioteca: " + label)
            elif not exact_case(destination):
                errors.append("Capitalização incorreta: " + label)
            elif parsed.fragment and destination.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(texts.get(destination, destination.read_text(encoding="utf-8-sig"))):
                    errors.append("Âncora ausente: " + label)
        if "[[" in content:
            errors.append("Referência Obsidian não convertida: " + path.relative_to(ROOT).as_posix())
        if re.search(r"(?im)^\s*(?:TODO|Em construção)\s*$", content):
            errors.append("Documento substituído por marcador: " + path.relative_to(ROOT).as_posix())
        fences = sum(bool(re.match(r"^\s*(`{3,}|~{3,})", line)) for line in body.splitlines())
        if fences % 2:
            errors.append("Bloco de código não fechado: " + path.relative_to(ROOT).as_posix())

    groups = defaultdict(list)
    for path in files:
        if path.stat().st_size == 0:
            errors.append("Arquivo vazio: " + path.relative_to(ROOT).as_posix())
        groups[digest(path)].append(path.relative_to(ROOT).as_posix())
        if path.name != "README.md" and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+)?", path.name):
            errors.append("Nome fora da convenção: " + path.relative_to(ROOT).as_posix())
        if path.suffix in {".zip", ".docx"}:
            with ZipFile(path) as archive:
                bad = archive.testzip()
                if bad:
                    errors.append("CRC inválido: " + str(path) + ": " + bad)
    for directory in ROOT.rglob("*"):
        if directory.is_dir() and ".git" not in directory.relative_to(ROOT).parts:
            if not any(directory.iterdir()):
                errors.append("Diretório vazio: " + directory.relative_to(ROOT).as_posix())
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", directory.name):
                errors.append("Nome de diretório fora da convenção: " + directory.relative_to(ROOT).as_posix())

    manifest = json.loads((ROOT / "recursos/referencias/manifesto-migracao.json").read_text(encoding="utf-8"))
    movements = {m["origem"]: m for m in manifest["movimentos"]}
    binaries = 0
    for source, expected in manifest["estado-inicial"].items():
        if Path(source).suffix.lower() not in {".zip", ".pdf", ".docx", ".png", ".jpg", ".jpeg"}:
            continue
        destination = ROOT / movements.get(source, {}).get("destino", source)
        binaries += 1
        if not destination.exists() or digest(destination) != expected:
            errors.append("Hash de binário divergente: " + destination.relative_to(ROOT).as_posix())
    for entry in manifest["origens"]:
        archive_path = ROOT / movements[entry["arquivo"]]["destino"]
        with ZipFile(archive_path) as archive:
            data = archive.read(entry["entrada"])
        if sha256(data).hexdigest() != entry["sha256-origem"]:
            errors.append("Origem divergente: " + entry["entrada"])
        destination = ROOT / entry["destino"]
        if not destination.exists() or destination.stat().st_size == 0:
            errors.append("Destino original ausente/vazio: " + entry["destino"])
        elif destination.suffix != ".md" and digest(destination) != entry["sha256-origem"]:
            errors.append("Destino binário original divergente: " + entry["destino"])

    metadata_count = 0
    for history in manifest.get("historicos-git", []):
        backup = ROOT / history["arquivo"]
        if not backup.exists() or digest(backup) != history["sha256"]:
            errors.append("Backup de metadados Git divergente: " + history["arquivo"])
            continue
        with ZipFile(backup) as archive:
            for name, expected in history["sha256-metadados"].items():
                metadata_count += 1
                if sha256(archive.read(".git/" + name)).hexdigest() != expected:
                    errors.append("Metadado Git divergente: " + history["arquivo"] + ": " + name)

    duplicates = [paths for paths in groups.values() if len(paths) > 1]
    result = {"arquivos": len(files), "markdown": len(texts), "links-locais": local_links,
              "binarios-preservados": binaries, "entradas-originais": len(manifest["origens"]),
              "metadados-git-preservados": metadata_count, "repositorios-embutidos": len(nested_git),
              "duplicacoes-de-bytes": duplicates, "erros": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors or duplicates else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
