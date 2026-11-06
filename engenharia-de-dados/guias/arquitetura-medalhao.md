# Arquitetura em camadas (medalhão)

Medalhão é o nome popular para separar o dado em Bronze, Silver e Gold. Aqui ele convive com o vocabulário do [Analytics Engineering](../../analytics-engineering/guias/arquitetura-e-camadas.md) (raw, staging, marts). A tabela abaixo traduz um no outro.

```text
Fonte → Bronze (Parquet) → RAW (DuckDB) → Silver (staging) → Gold (marts) → consumo
```

## Camadas

| Medalhão | Vocabulário do toolkit | Onde vive | Quem escreve | Contém |
|---|---|---|---|---|
| Bronze | arquivos de origem | Parquet em `data/bronze/` | Python (ingestão) | Dado como veio, mais metadados |
| RAW | raw | schema `raw` no DuckDB | Python (carga) | Espelho do Bronze em tabelas |
| Silver | staging (e intermediate, se precisar) | schema `staging` | dbt | Uma fonte por modelo, renomeada, tipada e padronizada |
| Gold | marts | schema `marts` | dbt | Fatos e dimensões com grão declarado |

**Por que Bronze e RAW?** O Bronze é o arquivo durável, fora do banco: permite recriar o banco inteiro. O RAW é o ponto de entrada do dbt, em tabelas SQL. Se a RAW não agregar nada ao seu projeto, registre a decisão e remova: camada não se mantém por hábito.

## O que cada camada pode e não pode

| Camada | Pode | Não pode |
|---|---|---|
| Bronze | Acrescentar metadados e particionar | Renomear, filtrar, corrigir ou aplicar regra |
| RAW | Ser recriada a partir do Bronze | Aplicar regra de negócio ou deduplicar |
| Silver | Renomear, tipar, padronizar e deduplicar por chave com regra documentada | Juntar fontes ou calcular métricas |
| Gold | Juntar, agregar e definir métricas, sempre com grão declarado e testado | Deixar cada relatório recalcular a métrica por conta própria |

## Nomes

| Camada | Padrão | Exemplo |
|---|---|---|
| Bronze | `data/bronze/<source>/<entity>/reference_date=AAAA-MM-DD/data.parquet` | `data/bronze/ons/load/reference_date=2026-01-02/data.parquet` |
| RAW | `raw.<source>__<entity>` | `raw.ons__load` |
| Silver | `stg_<source>__<entity>` | `stg_ons__load` |
| Gold | `fct_<processo>`, `dim_<conceito>` | `fct_daily_load` |

Os schemas `raw`, `staging` e `marts` ficam sem prefixo graças ao macro `generate_schema_name` do [template-projeto](../../template-projeto/dbt/macros/generate_schema_name.sql).

## Parquet na prática

- Particione pela data de referência, que é a unidade de reprocesso.
- Em projeto pequeno, um arquivo por partição basta. Evite milhares de arquivos minúsculos.
- Na Bronze, grave o que a fonte entregou. Se tudo vier como texto (CSV), mantenha texto e converta na Silver.

## O que apaga o quê

Bronze e RAW são reproduzíveis **se a fonte guarda histórico**. Se não guarda, a Bronze é a única cópia do passado: não a apague e mantenha um backup fora da máquina. O `make clean` do template apaga tudo, então use-o sabendo disso.

## Limite do DuckDB local

Um arquivo DuckDB aceita um processo escritor por vez (vários só leem). Isso serve para um projeto individual. Reconsidere o banco quando precisar de vários escritores simultâneos ou de acesso concorrente de várias pessoas, e registre a troca em `docs/02-arquitetura.md`.

**Pronto para avançar:** você sabe dizer em que camada cada regra vive, e apagar o banco local e rodar o pipeline o recria. Próximo passo: [orquestração com Airflow](orquestracao-airflow.md), só depois de rodar tudo à mão.

[Voltar à Engenharia de Dados](../README.md).
