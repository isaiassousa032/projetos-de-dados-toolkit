# Referências e acervo

Fontes para estudo e confirmação técnica. Documentação de ferramentas deve corresponder à versão e ao adaptador do projeto. Links oficiais abaixo foram consultados em **09/10/2026**; páginas com versões móveis podem mudar posteriormente.

## Documentação oficial

| Tema | Fonte |
|---|---|
| Dependências e fontes dbt | [Sources](https://docs.getdbt.com/docs/build/sources) |
| Execução dbt | [Build](https://docs.getdbt.com/reference/commands/build) |
| Testes dbt | [Data tests](https://docs.getdbt.com/docs/build/data-tests) |
| Processamento incremental | [Incremental models](https://docs.getdbt.com/docs/build/incremental-models) |
| Semântica dbt | [Semantic models](https://docs.getdbt.com/docs/build/semantic-models) |
| Freshness Core v1 | [Source command](https://docs.getdbt.com/reference/commands/source) |
| Orquestração | [Boas práticas do Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) |
| Modelagem dimensional | [Técnicas do Kimball Group](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) |
| Versionamento | [Git Reference](https://git-scm.com/docs) |
| CI/CD | [GitHub Actions](https://docs.github.com/en/actions) |
| Python | [Documentação oficial](https://docs.python.org/3/) |
| BI | [Microsoft Power BI](https://learn.microsoft.com/pt-br/power-bi/) |

Outras opções por finalidade estão no [índice de ferramentas](../ferramentas/README.md).

## Bibliografia

- Rui Machado e Helder Russa. **Analytics Engineering with SQL and dbt**. O'Reilly Media, 2023. [Página oficial da editora](https://www.oreilly.com/library/view/analytics-engineering-with/9781098142377/). Identificação bibliográfica confirmada; o livro completo não foi fornecido nem analisado nesta implementação.
- Ralph Kimball e Margy Ross. **The Data Warehouse Toolkit**, 3ª edição. Wiley, 2013. [Página oficial do Kimball Group](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/). Referência para estudo dimensional; o livro completo não faz parte do acervo local.

## Materiais de apoio

| Material | Identificação e uso |
|---|---|
| [Guia geral de Analytics Engineering](materiais/guia-geral-analytics-engineering.pdf) | 13 páginas; guia em português usado como apoio à síntese metodológica. Menciona inspiração no livro de Machado e Russa; isso não representa inspeção independente das páginas do livro citadas nele. |
| [The Analytics Development Lifecycle](https://www.getdbt.com/resources/guides/the-analytics-development-lifecycle) | Whitepaper da dbt Labs sobre o ciclo de desenvolvimento e operação de analytics. Apenas o link: o PDF não é redistribuído. |

Materiais de terceiros, como anotações de cursos, não ficam no repositório. Eles trazem exemplos dependentes de versão: para código real, use a documentação oficial e reveja argumentos de testes, configuração de snapshots, comando de full refresh e sintaxe Jinja.

Este acervo não tem licença atribuída. Antes da publicação externa, confirme a origem e a permissão de redistribuição do guia geral em PDF.

## Histórico

O estado anterior à limpeza de 05/11/2026 (ZIPs originais dos frameworks, manifesto de hashes e relatório de migração) está no histórico do Git deste repositório.

[Voltar aos recursos](../README.md).
