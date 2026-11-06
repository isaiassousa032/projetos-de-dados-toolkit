# Arquitetura

```text
Fonte → Python → Bronze (Parquet) → Python → RAW (DuckDB) → dbt → Silver (staging) → dbt → Gold (marts) → Power BI
```

## Camadas

| Camada | Onde vive | Quem escreve | Regra |
|---|---|---|---|
| Bronze | `data/bronze/` (Parquet) | `src/ingestion/` | Dado como veio da fonte, mais `_source` e `_ingested_at`. Sem regra de negócio |
| RAW | schema `raw` (DuckDB) | `src/load/` | Espelho do Bronze, recriado a cada carga. Sem regra de negócio |
| Silver | schema `staging` | dbt (`models/staging`) | Renomear, tipar e padronizar uma fonte por vez. Sem joins entre fontes |
| Gold | schema `marts` | dbt (`models/marts`) | Fatos e dimensões com grão declarado e testado. É o que o Power BI lê |

## Decisões

| Decisão | Escolha | Motivo | Alternativa descartada |
|---|---|---|---|
| Ingestão | Python | [preencha] | [preencha] |
| Formato Bronze | Parquet | [preencha] | [preencha] |
| Banco analítico | DuckDB local | [preencha] | [preencha] |
| Transformação | dbt | [preencha] | [preencha] |
| Orquestração | Airflow (fase 06) | [preencha] | [preencha] |
| Consumo | Power BI | [preencha] | [preencha] |

## Limites conhecidos

- [ex.: a fonte não tem histórico antes de AAAA]
- [ex.: atualizações tardias da fonte não são recapturadas]
