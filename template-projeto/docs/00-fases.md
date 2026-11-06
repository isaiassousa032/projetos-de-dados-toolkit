# Plano de fases

Siga na ordem. Só marque uma fase quando o critério "Pronto quando" for verdadeiro; se não for, a fase seguinte vai esconder o problema.

| # | Fase | Entrega | Pronto quando | Feito |
|---|---|---|---|---|
| 01 | Negócio | `docs/01-negocio.md` | Você explica em duas frases a decisão que os dados apoiam, e há ao menos uma métrica com fórmula e grão | [ ] |
| 02 | Arquitetura | `docs/02-arquitetura.md` | Sabe-se de onde cada dado vem e em que camada cada regra é aplicada | [ ] |
| 03 | Bronze | `src/ingestion/` | Rodar a mesma data duas vezes não duplica; um backfill de intervalo funciona | [ ] |
| 04 | RAW | `src/load/` | A tabela RAW é recriada do Bronze sem passo manual e a contagem confere | [ ] |
| 05 | Silver e Gold | `dbt/models/` | `dbt build` verde, grão do Gold declarado e testado, um número reconciliado com a fonte por outro caminho | [ ] |
| 06 | Airflow | `airflow/dags/` | A DAG executa o pipeline e um backfill sem intervenção. Só comece com 03 a 05 funcionando à mão | [ ] |
| 07 | CI/CD e docs | `.github/workflows/`, `make docs` | Um teste quebrado reprova o CI; a documentação do dbt é gerada | [ ] |
| 08 | Power BI | painel | O painel lê só o Gold e cada métrica bate com a definição da fase 01 | [ ] |
| 09 | Validação e publicação | README final | Um clone limpo reproduz o resultado seguindo só o README; não há segredos no repositório | [ ] |

## Referências no toolkit (consulte quando chegar na fase)

- 01: `compartilhado/guias/definicao-problema-negocio.md`, `analytics-engineering/templates/definicao-metricas-negocio.md`
- 02: `engenharia-de-dados/guias/arquitetura-medalhao.md`, `analytics-engineering/guias/arquitetura-e-camadas.md`
- 03 e 04: `engenharia-de-dados/guias/ingestao-idempotente.md`, `engenharia-de-dados/guias/arquitetura-medalhao.md`
- 05: `analytics-engineering/guias/boas-praticas-dbt.md`, `modelagem-de-dados.md`, `testes-e-qualidade.md`, `checklists/revisao-modelos-dbt.md`
- 06: `engenharia-de-dados/guias/orquestracao-airflow.md` (traz uma DAG testada), `analytics-engineering/guias/deploy-ci-cd-monitoramento.md`
- 07: `recursos/dataops/ci-cd-e-monitoramento.md`, `analytics-engineering/guias/documentacao-e-lineage.md`
- 09: `engenharia-de-dados/checklists/checklist-pipeline.md`, `analytics-engineering/checklists/deploy-entrega-final.md`, `checklists/qualidade-dados.md`
