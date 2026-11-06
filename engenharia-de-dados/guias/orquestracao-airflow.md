# Orquestração com Airflow

O orquestrador agenda, ordena, repete e registra execuções. Ele **não** substitui o pipeline: a DAG apenas chama passos que já funcionam à mão. Se `make all` ainda não termina verde, volte ao [guia de ingestão](ingestao-idempotente.md) antes de abrir o Airflow.

## Quando adotar

Adote quando precisar de execução agendada com dependências entre passos, retentativas e histórico de execuções. Para rodar uma única vez, ou quando um agendamento simples resolve (cron ou um workflow agendado do GitHub Actions), o Airflow só acrescenta manutenção.

## Seis princípios

1. **Tarefa pequena e idempotente.** Uma responsabilidade por tarefa, segura para repetir. É isso que torna a retentativa inofensiva. Divida por fronteira recuperável: ingestão → carga → transformação e testes → verificação do consumo.
2. **A data vem do agendamento, não do relógio.** Use `{{ ds }}` (a data do intervalo) e nunca a data de hoje dentro do script. Assim, reexecutar ou fazer backfill produz o mesmo resultado.
3. **A DAG só orquestra.** A lógica fica em `src/` e `dbt/`; a DAG chama. Mantenha o arquivo da DAG leve, sem importar bibliotecas pesadas no topo.
4. **Backfill é deliberado.** Deixe `catchup=False` explícito e reprocesse datas com `airflow backfill create --dag-id <dag> --from-date <início> --to-date <fim>`.
5. **Concorrência compatível com o banco.** DuckDB aceita um escritor por vez, então `max_active_runs=1`.
6. **Segredos fora da DAG.** Use connections ou variáveis de ambiente do Airflow, nunca texto no código.

## Exemplo

Cadeia Bronze → RAW → dbt, no mesmo padrão do [template-projeto](../../template-projeto/README.md). Fica em `airflow/dags/`.

```python
"""DAG do pipeline: Bronze -> RAW -> dbt. Cada tarefa chama um passo que já roda à mão."""

import os
from datetime import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

PROJECT_DIR = os.environ.get("PROJECT_DIR", "/opt/airflow/project")

with DAG(
    dag_id="project_pipeline",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,        # backfill é explícito: `airflow backfill create`
    max_active_runs=1,    # o DuckDB aceita um escritor por vez
    default_args={"retries": 2},
    tags=["pipeline"],
) as dag:
    ingest = BashOperator(
        task_id="ingest_bronze",
        bash_command="python -m src.ingestion.extract_example --start {{ ds }} --end {{ ds }}",
        cwd=PROJECT_DIR,
    )
    load = BashOperator(
        task_id="load_raw",
        bash_command="python -m src.load.load_raw",
        cwd=PROJECT_DIR,
    )
    transform = BashOperator(
        task_id="dbt_build",
        bash_command="dbt build --project-dir dbt --profiles-dir dbt",
        cwd=PROJECT_DIR,
    )

    ingest >> load >> transform
```

Este exemplo foi executado com Airflow 3.3.2 (`airflow dags test`): as três tarefas concluem e `{{ ds }}` vira a data do intervalo. Confira a documentação da versão que você instalou, porque importações e comandos mudam entre versões.

**Requisitos do ambiente:** Python, `dbt` e as dependências do projeto instalados no mesmo ambiente que executa as tarefas, e o projeto disponível em `PROJECT_DIR` (por exemplo, montado como volume no container).

## Erros comuns

| Erro | Sintoma | Correção |
|---|---|---|
| Usar a data de hoje no script | O backfill grava o dado do dia errado | Passe `{{ ds }}` como parâmetro |
| `catchup` ligado sem querer | Centenas de execuções ao ativar a DAG | `catchup=False` e backfill explícito |
| Duas execuções escrevendo no DuckDB | Erro de bloqueio do arquivo | `max_active_runs=1` |
| Lógica pesada no arquivo da DAG | Agendador lento, DAG demora a aparecer | Mover a lógica para `src/` |

Referência oficial: [boas práticas do Airflow](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html). Para alertas e sinais de falha, veja [monitoramento](../../recursos/dataops/ci-cd-e-monitoramento.md#monitoramento). Para a visão de deploy, veja [deploy, CI/CD e monitoramento](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md).

**Pronto para avançar:** a DAG executa o pipeline sem intervenção e reexecutar uma data não duplica nada. Feche com o [checklist de pipeline](../checklists/checklist-pipeline.md).

[Voltar à Engenharia de Dados](../README.md).
