# Índice de ferramentas

Escolha ferramentas após definir problema, fonte e consumo. Este índice organiza possibilidades; não determina uma stack obrigatória. Os links levam à documentação oficial, consultada em 09/10/2026. Use a versão correspondente ao projeto.

| Finalidade | Opções/referência | Critério de escolha |
|---|---|---|
| Ingestão | [Airbyte](https://docs.airbyte.com/), extração própria com [Python](https://docs.python.org/3/) | Conector, captura de mudanças/exclusões, retries e esforço de manutenção |
| Transformação | [dbt](https://docs.getdbt.com/docs/build/sources), SQL, Python | Reutilização, dependências, teste e habilidade da equipe |
| Armazenamento e consulta local | [DuckDB](https://duckdb.org/docs/stable/) | Volume, formatos locais e necessidade de compartilhar execução |
| Banco relacional | [PostgreSQL](https://www.postgresql.org/docs/) | Concorrência, integridade, operação e padrão de consulta |
| Data Warehouse | Plataforma existente ou DW gerenciado escolhido no projeto | Custo, escala, adaptação dbt, segurança e isolamento; não há fornecedor obrigatório |
| Orquestração | [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html), agendamento simples já disponível | Dependências entre sistemas, backfill e complexidade operacional |
| BI e consumo | [Power BI](https://learn.microsoft.com/pt-br/power-bi/), consultas SQL e notebooks Python | Público, distribuição, definição de métricas e governança |
| Qualidade | [Data tests dbt](https://docs.getdbt.com/docs/build/data-tests), [Great Expectations](https://docs.greatexpectations.io/docs/home/), asserções SQL | Regras relevantes, integração, evidência e resposta à falha |
| Versionamento | [Git](https://git-scm.com/doc) | Revisão, histórico e colaboração |
| CI/CD | [GitHub Actions](https://docs.github.com/en/actions) ou serviço adotado pela equipe | Isolamento, segredos, cobertura, custo e promoção |

Um banco relacional ou engine local pode atender estudos e recortes pequenos; o projeto deve avaliar se a operação e o consumo exigem DW compartilhado. Airflow entra quando automação entre sistemas justifica o custo, após demonstrar que o pipeline funciona.

Para escolher, registre necessidade, alternativas, compatibilidade, custo operacional e como validar a opção. Utilize o [template de decisão](../../analytics-engineering/templates/decisoes-arquiteturais.md).
