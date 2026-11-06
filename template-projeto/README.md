# [Nome do projeto]

[Uma frase: qual decisão estes dados apoiam e para quem.]

> **Como usar este template** (apague este bloco depois de copiar)
>
> 1. Copie a pasta `template-projeto/` para um repositório novo e renomeie.
> 2. `cp .env.example .env`, crie um ambiente virtual e rode `make setup`.
> 3. Rode `make all`. Se terminar verde, o esqueleto funciona na sua máquina.
> 4. Siga `docs/00-fases.md` na ordem. Preencha `docs/01-negocio.md` **antes** de trocar o exemplo pela fonte real.
> 5. Troque `src/ingestion/extract_example.py` pela sua fonte e renomeie `example_source` em todos os lugares (`src/`, `dbt/models/`).

## Fluxo

```text
Fonte → Python → Bronze (Parquet) → Python → RAW (DuckDB) → dbt → Silver (staging) → dbt → Gold (marts) → Power BI
```

Detalhes e decisões em [docs/02-arquitetura.md](docs/02-arquitetura.md). Progresso em [docs/00-fases.md](docs/00-fases.md).

## Comandos

Rode sempre a partir da raiz do repositório.

| Comando | O que faz |
|---|---|
| `make setup` | Instala as dependências (`requirements.txt`) |
| `make ingest` | Grava a camada Bronze (Parquet). Intervalo: `make ingest START=2026-01-01 END=2026-01-31` |
| `make load` | Recria as tabelas RAW no DuckDB a partir do Bronze |
| `make transform` | `dbt build`: constrói Silver e Gold e roda os testes |
| `make all` | Os três passos acima, em ordem |
| `make docs` | Gera e abre a documentação do dbt |
| `make clean` | Apaga Bronze, banco local e artefatos do dbt. Cuidado: se a fonte não guarda histórico, a Bronze é a única cópia do passado |

Sem `make` (Windows): rode os comandos do [Makefile](Makefile) diretamente.

## Estrutura

```text
├── src/ingestion/     # Fonte → Bronze (Parquet)
├── src/load/          # Bronze → RAW (DuckDB)
├── dbt/               # Silver (staging) e Gold (marts), testes
├── airflow/dags/      # Fase 06: só depois que 03–05 funcionarem à mão (DAG de exemplo no guia de orquestração do toolkit)
├── docs/              # negócio, arquitetura, plano de fases
├── data/bronze/       # Parquet local (fora do Git)
├── warehouse/         # banco DuckDB local (fora do Git)
└── .github/           # CI e Dependabot
```

## Convenções

- **Idioma:** documentação em português; código, tabelas e colunas em inglês; commits em inglês no padrão Conventional Commits (`feat: add ONS ingestion`).
- **Nomes:** RAW `raw.<source>__<entity>`; Silver `stg_<source>__<entity>`; Gold `fct_*` e `dim_*`.
- **Ingestão:** idempotente (rodar de novo não duplica), escrita atômica, falha alta se a fonte vier vazia, backfill por intervalo.
- **Grão:** todo modelo Gold declara "uma linha por…" na descrição e tem teste de unicidade nesse grão.
- **Segredos:** só em `.env` (fora do Git). Nunca em código, logs ou commits.
- **Versões:** `requirements.txt` fixa as versões testadas. Atualize de propósito, não por acidente.
