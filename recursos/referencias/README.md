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

## Materiais fornecidos no workspace

| Material preservado | Identificação e uso |
|---|---|
| [Guia geral de Analytics Engineering](materiais/guia-geral-analytics-engineering.pdf) | 13 páginas; guia em português fornecido, usado como apoio à síntese metodológica. Menciona inspiração no livro de Machado e Russa; isso não representa inspeção independente das páginas do livro citadas nele. |
| [dbt Fundamentals — DataCamp](materiais/dbt-fundamentals-datacamp.pdf) | 37 páginas; arquivo de anotações/transcrições fornecido. Material de estudo, não documentação oficial de uma versão atual. |
| [The Analytics Development Lifecycle](materiais/the-analytics-development-lifecycle.pdf) | 18 páginas; documento ADLC com carta de Tristan Handy datada de setembro de 2024. Apoio ao ciclo de desenvolvimento e operação. |
| [Imagem ADLC](../dataops/imagens/ciclo-de-vida-analitico-adlc.png) | Imagem fornecida; origem externa/licença não estabelecidas nesta implementação. |

Os binários foram mantidos sem conversão ou alteração. Não há licença nova atribuída a este acervo; antes da publicação externa, confirme permissão de redistribuição dos materiais de terceiros.

As anotações dbt apresentam exemplos dependentes de versão e formatação de transcrição. Para código real, use documentação oficial: reveja argumentos de testes, configuração de snapshots, comando de full refresh e sintaxe Jinja. Não alteramos o PDF original para corrigir essas diferenças.

## Originais e rastreabilidade

- [Framework Completo original](originais/framework-analise-de-dados-main.zip).
- [Framework Lite original](originais/framework-analise-de-dados-lite-main.zip).
- [Metadados e histórico Git do Completo](originais/framework-completo-metadados-git.zip).
- [Metadados e histórico Git do Lite](originais/framework-lite-metadados-git.zip).
- [Manifesto de hashes e destinos](manifesto-migracao.json).
- [Relatório de diagnóstico, migração e validação](relatorio-migracao.md).

Os ZIPs são cópias de recuperação intencionalmente preservadas. A documentação ativa usa os destinos organizados e links relativos; não é necessário extrair os ZIPs para utilizar o toolkit.

Os `.git` internos foram retirados das pastas ativas após preservação integral, para evitar repositórios embutidos no Git central. Os dois backups de metadados contêm 77 arquivos verificados por hash e conservam os históricos sem reescrita. Para recuperar um repositório original, extraia seu ZIP de conteúdo em uma pasta separada e extraia o ZIP de metadados correspondente nessa pasta, produzindo `.git/`; mantenha a recuperação fora da biblioteca ativa. Confirme o HEAD e o estado com Git antes de retomar trabalho.

[Voltar aos recursos](../README.md).
