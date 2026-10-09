# Método de Análise de Dados

Repositório com **guias e modelos reutilizáveis** para estruturar análises de dados do entendimento à decisão.

O objetivo é manter um processo **simples, consistente e independente de ferramentas** (SQL, Python, Power BI, Excel etc.).

---

## Fluxo do método

```text
Dados / Problema
      ↓
   ENTENDER
      ↓
   ANALISAR
      ↓
  COMUNICAR
      ↓
   DECISÃO
```

1. **Entender** — compreender problema e dados
2. **Analisar** — investigar hipóteses com evidências
3. **Comunicar** — transformar em insights e recomendações

---

## Estrutura

```text
analise-de-dados/completo/
├── guias/
├── templates/
└── exemplos/
```

---

# 1. Entender

Antes de analisar, é preciso entender **o que os dados representam e qual problema será resolvido**.

## Guia

[`guia-primeiras-perguntas.md`](../../compartilhado/guias/guia-primeiras-perguntas.md)

Perguntas essenciais:

- Qual o problema de negócio?
- O que uma linha representa?
- Qual a granularidade?
- Quais são as chaves e métricas?
- Existem limitações ou inconsistências?

## Modelo

[`template-diagnostico-inicial.docx`](templates/template-diagnostico-inicial.docx)

---

# 2. Analisar

Fluxo de investigação:

```text
Problema → Pergunta → Hipóteses → Evidências → Insights → Recomendações → Decisão
```

## Guia

[`framework-analise-de-dados.md`](guias/framework-analise-de-dados.md)

Inclui:

- definição da pergunta
- hipóteses
- validação
- evidências
- insights e recomendações

## Modelo

[`template-framework-analise.docx`](templates/template-framework-analise.docx)

---

# 3. Comunicar

Transformar análise em decisão:

> O que foi descoberto, por que importa e o que fazer.

## Modelo

[`template-resumo-executivo.docx`](templates/template-resumo-executivo.docx)

Inclui:

- problema e objetivo
- insights principais
- evidências
- recomendações
- próximos passos

---

# Como usar

1. **Entender** → usar guia + diagnóstico inicial
2. **Analisar** → usar framework + modelo de análise
3. **Comunicar** → usar resumo executivo

---

# Exemplos

A pasta [`exemplos/`](exemplos/) orienta o registro de casos aplicados. Os originais não incluem projetos concluídos; consulte o exemplo ilustrativo adicionado nesta biblioteca.

---

# Princípios

- **Não começar pela ferramenta** → comece pelo problema
- **Número precisa de contexto** → sempre comparar
- **Insight = achado + impacto + recomendação**
- **Análise termina quando responde a pergunta inicial**

---

## Regra mental

```text
Por quê? → problema
O quê? → dados
Quem/Onde/Quando? → contexto
Quanto? → métricas
Comparado a quê? → referência
Por quê aconteceu? → hipóteses
E daí? → decisão
```

---

## Objetivo

Um método pessoal que evolui com a prática:

> **Entender → Analisar → Comunicar → Decidir**

## Navegação no toolkit

Use o Completo quando houver múltiplas hipóteses, fontes, recortes ou necessidade de comunicação executiva. Os três templates Word acima foram preservados sem alteração de bytes. O guia contém também template de nota e checklists de investigação e encerramento, evitando documentos repetidos.

- [Problema de negócio](../../compartilhado/guias/definicao-problema-negocio.md), para delimitar a decisão.
- [Qualidade de dados](../../compartilhado/guias/qualidade-de-dados.md), para aprofundar riscos encontrados no diagnóstico.
- [Exemplo ilustrativo de receita por canal](exemplos/analise-receita-por-canal.md).
- [Lite](../lite/README.md), para análises curtas.
- [Analytics Engineering](../../analytics-engineering/README.md), para modelos recorrentes usados pela análise.

Copie os templates para o repositório do projeto. As referências e exemplos deste toolkit não substituem evidências produzidas sobre a base real.

[Voltar à área de Análise de Dados](../README.md) ou ao [toolkit](../../README.md).
