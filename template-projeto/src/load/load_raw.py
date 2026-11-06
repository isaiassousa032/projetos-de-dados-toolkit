"""Carga RAW: lê o Parquet (Bronze) e recria a tabela no DuckDB.

A carga é completa a partir do Bronze, então é idempotente: rodar duas vezes
produz o mesmo resultado. Sem regra de negócio aqui; isso é papel do dbt.

Uso (na raiz do repositório):
    python -m src.load.load_raw
"""

import duckdb

from src.config import BRONZE_DIR, WAREHOUSE_PATH
from src.ingestion.extract_example import ENTITY, SOURCE


def main() -> None:
    pattern = (BRONZE_DIR / SOURCE / ENTITY / "*" / "data.parquet").as_posix()
    table = f"raw.{SOURCE}__{ENTITY}"

    WAREHOUSE_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(WAREHOUSE_PATH))
    try:
        con.execute("create schema if not exists raw")
        con.execute(
            f"create or replace table {table} as "
            f"select * from read_parquet('{pattern}', hive_partitioning=false)"
        )
        rows = con.execute(f"select count(*) from {table}").fetchone()[0]
    finally:
        con.close()

    if rows == 0:
        raise RuntimeError(f"{table} ficou vazia; verifique a camada Bronze.")
    print(f"raw ok: {table} ({rows} linhas)")


if __name__ == "__main__":
    main()
