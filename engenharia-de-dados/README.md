# Engenharia de Dados

Guias para levar dados da fonte até o banco analítico de forma repetível: ingestão, camadas e orquestração. Esta área termina onde o [Analytics Engineering](../analytics-engineering/README.md) começa: a partir da tabela RAW, quem modela é o dbt.

## Quando usar

Use quando o projeto precisa buscar dados de uma fonte, guardar histórico e atualizar com frequência (caminho B do [comece-aqui](../comece-aqui.md)). Para analisar dados que já estão prontos, esta área não é necessária.

## Roteiro

1. Entenda o que vive em cada camada na [arquitetura em camadas (medalhão)](guias/arquitetura-medalhao.md).
2. Construa a ingestão seguindo o [guia de ingestão idempotente](guias/ingestao-idempotente.md).
3. Faça o pipeline inteiro rodar à mão (`make all` no [template-projeto](../template-projeto/README.md)).
4. Só então automatize, com o [guia de orquestração com Airflow](guias/orquestracao-airflow.md).
5. Antes de dar por pronto, passe o [checklist de pipeline](checklists/checklist-pipeline.md).

## Padrão adotado

```text
Fonte → Python → Bronze (Parquet) → Python → RAW (DuckDB) → dbt → Silver → dbt → Gold
```

Os guias descrevem esse padrão e dizem quando faz sentido trocar uma peça. O [template-projeto](../template-projeto/README.md) traz o mesmo fluxo funcionando, com dados de exemplo.

## Fora do escopo

Streaming, Spark e ferramentas gerenciadas de ingestão não são tratados aqui. Entram só quando um requisito concreto (volume, latência, fonte sem alternativa) justificar o custo extra.

## Apoio

[CI/CD e monitoramento](../recursos/dataops/ci-cd-e-monitoramento.md) estão em DataOps. Cargas incrementais no dbt estão em [materializações e incrementais](../analytics-engineering/guias/materializacoes-e-incrementais.md).

[Voltar ao toolkit](../README.md).
