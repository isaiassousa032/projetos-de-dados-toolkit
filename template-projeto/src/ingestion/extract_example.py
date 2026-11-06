"""Ingestão de exemplo (camada Bronze: Parquet).

Substitua `fetch_records` pela chamada real (API, arquivo, scraping). O resto
do padrão deve ser mantido:

- idempotente: rodar de novo a mesma data sobrescreve a partição, não duplica;
- escrita atômica: escreve em arquivo temporário e só então renomeia;
- falha alta: resposta vazia interrompe a execução em vez de gravar nada;
- metadados de rastreio: `_source` e `_ingested_at` em todas as linhas;
- backfill: --start e --end reprocessam qualquer intervalo de datas.

Uso (na raiz do repositório):
    python -m src.ingestion.extract_example --start 2026-01-01 --end 2026-01-03
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from src.config import BRONZE_DIR

SOURCE = "example_source"
ENTITY = "readings"


def fetch_records(reference_date: date) -> list[dict]:
    """Dados sintéticos e determinísticos. Troque pela fonte real."""
    return [
        {
            "reading_id": f"{reference_date:%Y%m%d}-{i}",
            "reference_date": reference_date,
            "station": f"S{i % 3}",
            "value": float(10 + i),
        }
        for i in range(6)
    ]


def write_bronze(records: list[dict], reference_date: date) -> Path:
    if not records:
        raise RuntimeError(f"Fonte retornou 0 registros para {reference_date}.")

    ingested_at = datetime.now(timezone.utc)
    table = pa.Table.from_pylist(records)
    table = table.append_column("_source", pa.array([SOURCE] * len(records)))
    table = table.append_column(
        "_ingested_at",
        pa.array([ingested_at] * len(records), type=pa.timestamp("us", "UTC")),
    )

    partition = BRONZE_DIR / SOURCE / ENTITY / f"reference_date={reference_date:%Y-%m-%d}"
    partition.mkdir(parents=True, exist_ok=True)
    final = partition / "data.parquet"
    tmp = partition / "data.parquet.tmp"
    pq.write_table(table, tmp)
    tmp.replace(final)  # troca atômica: nunca fica um arquivo pela metade
    return final


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--start", type=date.fromisoformat, required=True)
    parser.add_argument("--end", type=date.fromisoformat, required=True)
    args = parser.parse_args()
    if args.end < args.start:
        parser.error("--end deve ser maior ou igual a --start")

    current = args.start
    while current <= args.end:
        path = write_bronze(fetch_records(current), current)
        print(f"bronze ok: {path}")
        current += timedelta(days=1)


if __name__ == "__main__":
    main()
