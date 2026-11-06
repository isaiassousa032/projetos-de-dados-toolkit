.PHONY: setup ingest load transform docs all clean

PY ?= python
START ?= 2026-01-01
END ?= 2026-01-03
DBT = dbt --no-use-colors
DBT_ARGS = --project-dir dbt --profiles-dir dbt

setup:
	$(PY) -m pip install -r requirements.txt

ingest:
	$(PY) -m src.ingestion.extract_example --start $(START) --end $(END)

load:
	$(PY) -m src.load.load_raw

transform:
	$(DBT) build $(DBT_ARGS)

docs:
	$(DBT) docs generate $(DBT_ARGS)
	$(DBT) docs serve $(DBT_ARGS)

all: ingest load transform

clean:
	rm -rf data/bronze/* warehouse/* dbt/target dbt/logs
	touch data/bronze/.gitkeep warehouse/.gitkeep
