# Comece aqui

Se você vai começar um projeto de dados e não sabe por onde, leia só esta página. Ela escolhe o caminho por você e diz o que fazer hoje. O resto do toolkit é consulta: abra um documento quando chegar na etapa que o pede, não antes.

## 1. Escolha o caminho

| Sua situação | Caminho | Primeiro passo (hoje) |
|---|---|---|
| Os dados já estão prontos (CSV, tabela limpa) e eu quero responder uma pergunta | **A. Análise** | Copiar o [template Lite](analise-de-dados/lite/templates/template-analise-lite.md) e preencher "Entender" |
| Preciso buscar dados de uma fonte, guardar histórico e atualizar com frequência | **B. Pipeline ponta a ponta** | Copiar o [template-projeto](template-projeto/README.md) e rodar `make all` |
| Os dados já estão carregados e falta modelá-los (métricas, tabelas fato e dimensão) | **C. Modelagem** | Escrever o grão ("cada linha representa…") do primeiro modelo |

Em dúvida entre A e B: se você precisará rodar de novo na semana que vem com dados novos, é B.

## Caminho A: Análise

1. Uma base e perguntas delimitadas (até uns 5 dias): use o [Lite](analise-de-dados/lite/README.md). Várias hipóteses, recortes ou um resumo para decisão: use o [Completo](analise-de-dados/completo/README.md).
2. Base nova? Leia só as perguntas relevantes do [guia de primeiras perguntas](compartilhado/guias/guia-primeiras-perguntas.md).
3. Preencha o template **ao longo** da análise, não no fim.
4. Feche com o [checklist do projeto curto](analise-de-dados/lite/checklists/checklist-projeto-curto.md).

## Caminho B: Pipeline ponta a ponta

**Stack padrão** (já testada no [template-projeto](template-projeto/README.md)). Troque uma peça só com um motivo escrito em `docs/02-arquitetura.md`.

| Papel | Padrão |
|---|---|
| Ingestão | Python |
| Bronze | Parquet |
| RAW e banco analítico | DuckDB |
| Silver e Gold | dbt (adaptador dbt-duckdb) |
| Orquestração | Airflow, somente depois que o pipeline rodar à mão |
| CI | GitHub Actions |
| Consumo | Power BI, lendo só o Gold |
| Versionamento | Git, commits em inglês no padrão Conventional Commits |

Sequência:

1. Crie o repositório do projeto a partir do `template-projeto/` e rode `make all`. Verde significa que o esqueleto funciona.
2. Preencha `docs/01-negocio.md` **antes** de trocar o exemplo pela fonte real.
3. Siga o [plano de fases](template-projeto/docs/00-fases.md) na ordem. Cada fase tem um critério "Pronto quando" e aponta para os guias do toolkit que valem naquele momento. Ingestão, camadas e orquestração estão em [Engenharia de Dados](engenharia-de-dados/README.md).

## Caminho C: Modelagem

1. Registre o mínimo de requisitos: [levantamento](analytics-engineering/templates/levantamento-requisitos.md) e a primeira [métrica](analytics-engineering/templates/definicao-metricas-negocio.md).
2. Declare o grão antes de criar qualquer tabela fato. Veja [modelagem de dados](analytics-engineering/guias/modelagem-de-dados.md).
3. Construa staging e um mart, com testes. Revise com o [checklist de modelos dbt](analytics-engineering/checklists/revisao-modelos-dbt.md).
4. Visão completa do processo: [Analytics Engineering](analytics-engineering/README.md).

## Cinco regras que valem em qualquer caminho

1. **Pergunta antes de código.** Escreva a decisão que os dados apoiam. Sem ela, você está só mexendo em dados.
2. **Grão antes de tabela.** "Cada linha representa…" vem antes de qualquer fato.
3. **Funcionando à mão antes de automatizar.** Airflow e CI entram depois de o pipeline rodar sozinho em uma máquina.
4. **Todo número publicado é reconciliado** por um segundo caminho (outra consulta, a fonte, um cálculo manual).
5. **Nenhum segredo no Git.** Credenciais ficam em `.env`.

## O que não fazer

- Não preencha todos os templates. Use só os do caminho escolhido.
- Não aponte o projeto para arquivos deste toolkit com links relativos. Copie o que usar para o repositório do projeto.
- Não adicione ferramenta nova sem um problema concreto que ela resolva.

[Voltar ao toolkit](README.md).
