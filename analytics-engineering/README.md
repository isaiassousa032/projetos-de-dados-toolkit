# Analytics Engineering

Framework para transformar necessidades de negócio em modelos analíticos confiáveis e reutilizáveis. Comece por uma entrega pequena: uma fonte, um processo, um grão explícito e uma pergunta validada. Expanda após comprovar utilidade e qualidade.

## Roteiro

1. Consulte o [framework principal](guias/framework-analytics-engineering.md), que descreve doze atividades e seus critérios de prontidão.
2. Copie o [levantamento de requisitos](templates/levantamento-requisitos.md) e documente a primeira [métrica](templates/definicao-metricas-negocio.md).
3. Registre [modelagem dimensional](templates/modelagem-dimensional.md) e [decisões arquiteturais](templates/decisoes-arquiteturais.md) conforme a necessidade.
4. Desenvolva modelos no repositório do projeto, usando o [template de documentação dbt](templates/documentacao-modelos-dbt.md).
5. Revise os checklists pertinentes antes de compartilhar ou promover resultados.

Airflow é opcional e entra após o pipeline funcionar. Uma camada semântica também é opcional. Este diretório contém referências e trechos didáticos; não contém projeto dbt, DAG Airflow nem infraestrutura implantável.

## Guias práticos

- [Modelagem conceitual, lógica, física e dimensional](guias/modelagem-de-dados.md).
- [Arquitetura e separação de camadas](guias/arquitetura-e-camadas.md).
- [Boas práticas com dbt](guias/boas-praticas-dbt.md).
- [Testes e qualidade](guias/testes-e-qualidade.md).
- [Documentação e lineage](guias/documentacao-e-lineage.md).
- [Materializações e incrementais](guias/materializacoes-e-incrementais.md).
- [Camada semântica](guias/camada-semantica.md).
- [Deploy, CI/CD e monitoramento](guias/deploy-ci-cd-monitoramento.md).

## Checklists

- [Início do projeto](checklists/inicio-projeto.md).
- [Revisão da modelagem](checklists/revisao-modelagem.md).
- [Qualidade dos dados](checklists/qualidade-dados.md).
- [Revisão dos modelos dbt](checklists/revisao-modelos-dbt.md).
- [Deploy e entrega](checklists/deploy-entrega-final.md).

## Exemplos e apoio

O [exemplo dimensional de vendas](exemplos/modelagem-vendas.md) conecta grão, medidas e relacionamentos. Os [trechos dbt](exemplos/trechos-dbt.md) ilustram sources, staging e testes. As [consultas SQL](exemplos/consultas-analiticas.md) mostram validação e consumo com dados fictícios.

Consulte [problema e qualidade compartilhados](../compartilhado/README.md), [DataOps](../recursos/dataops/README.md) e [referências técnicas](../recursos/referencias/README.md). Os PDFs fornecidos foram preservados como apoio; a documentação operacional deve seguir a versão instalada das ferramentas.

[Voltar ao toolkit](../README.md).
