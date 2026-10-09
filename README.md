# projetos-de-dados-toolkit

Biblioteca de metodologias, guias, templates, checklists e referências para projetos de **Análise de Dados** e **Analytics Engineering**. Reúne os frameworks Lite e Completo existentes e um framework para desenvolver dados analíticos confiáveis, documentados e reutilizáveis.

O toolkit orienta projetos de portfólio e profissionais com SQL, Python, Power BI, dbt e Data Warehouses. Os códigos, dados e configurações de cada projeto ficam em repositórios próprios. Airflow e agentes de IA são recursos opcionais, adotados conforme a necessidade.

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

O [Framework Completo](analise-de-dados/completo/README.md) organiza **Entender → Analisar → Comunicar → Decidir**. Após o diagnóstico inicial, transforma o problema em perguntas, subperguntas e hipóteses, registra evidências e comunica insights e recomendações. Inclui os templates Word originais de diagnóstico, aplicação e resumo executivo.

### Analytics Engineering

O [Framework de Analytics Engineering](analytics-engineering/README.md) orienta requisitos, modelagem conceitual, lógica, física e dimensional, arquitetura, grão, DW, dbt, métricas, SQL, deploy e operação. As doze etapas são iterativas. Testes e documentação acompanham o desenvolvimento; a camada semântica e a orquestração avançada são opcionais.

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
├── analise-de-dados/
│   ├── README.md
│   ├── lite/             # guia, templates, checklist e imagem originais
│   └── completo/         # guia, templates Word e exemplos
├── analytics-engineering/
│   ├── README.md
│   ├── guias/
│   ├── templates/
│   ├── checklists/
│   └── exemplos/
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
| Iniciar uma análise rápida | [Guia Lite](analise-de-dados/lite/guias/framework-lite.md) e [template](analise-de-dados/lite/templates/template-analise-lite.md) |
| Compreender uma nova base | [Primeiras perguntas](compartilhado/guias/guia-primeiras-perguntas.md) |
| Investigar hipóteses | [Framework Completo](analise-de-dados/completo/guias/framework-analise-de-dados.md) |
| Construir modelos analíticos | [Framework de Analytics Engineering](analytics-engineering/guias/framework-analytics-engineering.md) |
| Definir métricas | [Template de métrica de negócio](analytics-engineering/templates/definicao-metricas-negocio.md) |
| Revisar qualidade | [Guia compartilhado](compartilhado/guias/qualidade-de-dados.md) |
| Revisar mudanças e operação | [DataOps](recursos/dataops/README.md) |
| Conferir a implementação | [Relatório de migração e validação](recursos/referencias/relatorio-migracao.md) |

## Contribuição e evolução

Proponha mudanças pequenas, com problema, conteúdo afetado, justificativa e validação. Use nomes em `kebab-case`, Markdown em português brasileiro e links relativos para documentos internos. Identificadores SQL e dbt seguem as [convenções](compartilhado/guias/convencoes-nomenclatura-documentacao.md).

Antes de criar um guia, procure um documento existente. Centralize regras compartilhadas e mantenha exemplos didáticos pequenos. Revise links, fontes, adequação dos templates e ausência de dados sensíveis. Mudanças metodológicas precisam explicar o efeito na prática; alterações de dbt devem considerar versão e adaptador.

Este trabalho não define uma licença. Verifique os direitos dos materiais de terceiros antes de redistribuí-los publicamente, especialmente PDFs de cursos. Não há credenciais, certificações ou resultados de projetos declarados aqui.

## Origem e preservação

Os dois frameworks foram encontrados nos ZIPs fornecidos no workspace e comparados com as cópias já organizadas. Os [arquivos originais](recursos/referencias/README.md) permanecem disponíveis para recuperação, e o [manifesto](recursos/referencias/manifesto-migracao.json) registra destinos e hashes. As adaptações de navegação estão descritas no relatório.

Os históricos Git encontrados dentro das pastas dos frameworks também foram preservados integralmente em arquivos de recuperação. As pastas ativas pertencem ao Git central, sem repositórios embutidos.

`projetos-de-dados-toolkit` é o nome desta biblioteca. O checkout local mantém o nome de pasta existente `projetos-de-dados-toolkit`; nenhuma configuração Git ou identidade remota foi alterada.
