# projetos-de-dados-toolkit

Biblioteca de metodologias, guias, templates, checklists e referências para projetos de **Análise de Dados**, **Engenharia de Dados** e **Analytics Engineering**. Reúne os frameworks Lite e Completo existentes e um framework para desenvolver dados analíticos confiáveis, documentados e reutilizáveis.

O toolkit orienta projetos de portfólio e profissionais com SQL, Python, Power BI, dbt e Data Warehouses. Os códigos, dados e configurações de cada projeto ficam em repositórios próprios. Airflow e agentes de IA são recursos opcionais, adotados conforme a necessidade.

> **Primeira vez aqui, ou sem saber por onde começar? Leia [comece-aqui.md](comece-aqui.md).** Ele escolhe o caminho e diz o que fazer hoje.

## Índice

- [Objetivos](#objetivos)
- [Áreas disponíveis](#áreas-disponíveis)
- [Qual framework utilizar](#qual-framework-utilizar)
- [Estrutura](#estrutura)
- [Como utilizar](#como-utilizar)
- [Documentos principais](#documentos-principais)
- [Contribuição e evolução](#contribuição-e-evolução)
- [Origem e preservação](#origem-e-preservação)

## Objetivos

- Começar pelo problema e pela decisão que os dados devem apoiar.
- Produzir evidências confiáveis e explicitar limites das conclusões.
- Separar investigação analítica de construção e operação de modelos reutilizáveis.
- Reaproveitar documentação sem aumentar a burocracia dos projetos pequenos.
- Manter uma biblioteca navegável, versionável e independente de fornecedor.

## Áreas disponíveis

### Análise de Dados — Lite

O [Framework Lite](analise-de-dados/lite/README.md) organiza **Entender → Perguntar → Analisar → Interpretar → Concluir**. Destina-se a análises rápidas, exercícios e explorações com escopo pequeno; o original sugere aproximadamente 1 a 5 dias, como orientação, não prazo obrigatório. Basta consultar o guia, preencher uma cópia do template e revisar o checklist final.

### Análise de Dados — Completo

O [Framework Completo](analise-de-dados/completo/README.md) organiza **Entender → Analisar → Comunicar → Decidir**. Após o diagnóstico inicial, transforma o problema em perguntas, subperguntas e hipóteses, registra evidências e comunica insights e recomendações. Inclui templates em Markdown de diagnóstico, aplicação e resumo executivo.

### Analytics Engineering

O [Framework de Analytics Engineering](analytics-engineering/README.md) orienta requisitos, modelagem conceitual, lógica, física e dimensional, arquitetura, grão, DW, dbt, métricas, SQL, deploy e operação. As doze etapas são iterativas. Testes e documentação acompanham o desenvolvimento; a camada semântica e a orquestração avançada são opcionais.

### Engenharia de Dados

A pasta [Engenharia de Dados](engenharia-de-dados/README.md) cobre a ingestão idempotente, a arquitetura em camadas (Bronze, RAW, Silver e Gold) e a orquestração com Airflow, até a entrega da tabela RAW ao dbt. O [template-projeto](template-projeto/README.md) traz esse fluxo completo funcionando, com dados de exemplo.

### Materiais compartilhados e recursos

[Compartilhado](compartilhado/README.md) concentra problema de negócio, requisitos, qualidade e convenções. [Recursos](recursos/README.md) reúne DataOps, índice de ferramentas, uso opcional de IA e referências de estudo.

## Qual framework utilizar

| Critério | Lite | Completo | Analytics Engineering |
|---|---|---|---|
| Necessidade principal | Resposta rápida e prática | Investigação estruturada para decisão | Dados confiáveis para consumo recorrente |
| Escopo típico | Uma base e poucas perguntas | Múltiplas hipóteses, recortes e stakeholders | Fontes, modelos, métricas e consumidores |
| Processo | Cinco etapas enxutas | Diagnóstico, investigação e comunicação | Doze atividades adaptáveis |
| Registro principal | Um template de análise | Diagnóstico, evidências e resumo executivo | Requisitos, modelos, decisões e métricas |
| Entrega | Conclusão com evidências e limites | Recomendações sustentadas e próximos passos | Modelos testados, documentados e operáveis |
| Automação | Conforme a necessidade | Conforme recorrência e risco | Evolui após a primeira entrega funcional |

Lite e Completo são independentes. Analytics Engineering pode preparar os modelos consumidos por qualquer um deles; não é pré-requisito para toda análise.

## Estrutura

```text
projetos-de-dados-toolkit/
├── README.md
├── comece-aqui.md         # ponto de partida: escolhe o caminho
├── template-projeto/     # esqueleto de projeto pronto para copiar (Python, DuckDB, dbt)
├── analise-de-dados/
│   ├── README.md
│   ├── lite/             # guia, templates, checklist e imagem originais
│   └── completo/         # guia, templates e exemplos
├── analytics-engineering/
│   ├── README.md
│   ├── guias/
│   ├── templates/
│   ├── checklists/
│   └── exemplos/
├── engenharia-de-dados/
│   ├── README.md
│   ├── guias/
│   └── checklists/
├── compartilhado/
│   ├── README.md
│   ├── guias/
│   └── templates/
└── recursos/
    ├── README.md
    ├── dataops/
    ├── ferramentas/
    ├── prompts-ia/
    └── referencias/       # fontes de estudo e registro da migração
```

## Como utilizar

1. Defina a decisão, a pergunta e o escopo. Consulte o [guia de problema de negócio](compartilhado/guias/definicao-problema-negocio.md).
2. Escolha o framework pela entrega esperada e abra seu README.
3. Copie somente os templates úteis para o repositório do projeto. Campos entre colchetes são instruções para preenchimento; marque itens não aplicáveis com justificativa.
4. Registre regras, evidências, responsáveis e limitações enquanto trabalha. Guarde consultas, notebooks, dashboards e pipelines no projeto correspondente.
5. Use o checklist compatível com a entrega. Valide o significado com o stakeholder e a correção técnica com verificações independentes.
6. Traga para esta biblioteca apenas melhorias generalizáveis, referências ou exemplos sanitizados e identificados como reais ou ilustrativos.

Ao copiar templates para outro repositório, adapte os links ao novo destino ou cite a versão do toolkit utilizada. Não é necessário preencher todos os templates para uma análise curta.

## Documentos principais

| Finalidade | Documento |
|---|---|
| Começar um projeto | [Comece aqui](comece-aqui.md) e [template de projeto](template-projeto/README.md) |
| Iniciar uma análise rápida | [Guia Lite](analise-de-dados/lite/guias/framework-lite.md) e [template](analise-de-dados/lite/templates/template-analise-lite.md) |
| Compreender uma nova base | [Primeiras perguntas](compartilhado/guias/guia-primeiras-perguntas.md) |
| Investigar hipóteses | [Framework Completo](analise-de-dados/completo/guias/framework-analise-de-dados.md) |
| Construir modelos analíticos | [Framework de Analytics Engineering](analytics-engineering/guias/framework-analytics-engineering.md) |
| Ingerir e orquestrar dados | [Engenharia de Dados](engenharia-de-dados/README.md) |
| Definir métricas | [Template de métrica de negócio](analytics-engineering/templates/definicao-metricas-negocio.md) |
| Revisar qualidade | [Guia compartilhado](compartilhado/guias/qualidade-de-dados.md) |
| Revisar mudanças e operação | [DataOps](recursos/dataops/README.md) |

## Contribuição e evolução

Proponha mudanças pequenas, com problema, conteúdo afetado, justificativa e validação. Use nomes em `kebab-case`, Markdown em português brasileiro e links relativos para documentos internos. Identificadores SQL e dbt seguem as [convenções](compartilhado/guias/convencoes-nomenclatura-documentacao.md).

Antes de criar um guia, procure um documento existente. Centralize regras compartilhadas e mantenha exemplos didáticos pequenos. Revise links, fontes, adequação dos templates e ausência de dados sensíveis. Mudanças metodológicas precisam explicar o efeito na prática; alterações de dbt devem considerar versão e adaptador.

Este trabalho não define uma licença. Confirme os direitos do guia geral em PDF antes de redistribuí-lo publicamente. Não há credenciais, certificações ou resultados de projetos declarados aqui.

## Origem e preservação

Os frameworks Lite e Completo foram incorporados a partir de projetos anteriores. O estado anterior à limpeza de 05/11/2026 (ZIPs originais, manifesto de hashes e relatório de migração) está no histórico do Git deste repositório.
