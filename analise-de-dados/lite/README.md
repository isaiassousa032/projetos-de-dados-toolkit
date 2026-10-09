# Framework de Análise de Dados — Lite

Framework enxuto para estruturar **projetos curtos de análise de dados**, com foco em prática, repetição do processo analítico e desenvolvimento do raciocínio sobre dados.

A proposta é aplicar um processo de análise completo sem adicionar documentação ou complexidade desnecessária.

> **Pequeno no escopo, completo no raciocínio.**

---

## Sobre o framework

O **Framework de Análise de Dados — Lite** foi criado como uma versão reduzida do meu framework principal de análise de dados.

Enquanto a versão completa é destinada principalmente a projetos médios e longos, esta versão foi pensada para análises rápidas, normalmente desenvolvidas entre **1 e 5 dias**.

O objetivo não é explorar todas as possibilidades de um dataset, mas responder a um conjunto claro de perguntas utilizando evidências.

O processo segue cinco etapas:

```text
Entender
   ↓
Perguntar
   ↓
Analisar
   ↓
Interpretar
   ↓
Concluir
```
---
![alt text](imagens/diagrama-fluxo-de-dados.png)
---

## Objetivo

O framework busca tornar mais frequente a prática do ciclo completo de análise:

**dados → perguntas → análise → evidências → conclusões**

Isso permite utilizar diferentes datasets, ferramentas e técnicas sem transformar cada análise em um projeto de grande duração.

Entre os principais objetivos estão:

- desenvolver raciocínio analítico;
- praticar análise exploratória de dados;
- melhorar a formulação de perguntas;
- aprender a selecionar métricas e dimensões relevantes;
- desenvolver interpretação de resultados;
- praticar diferentes técnicas de análise;
- experimentar diferentes ferramentas;
- comunicar conclusões de maneira objetiva.

---

## Quando usar

Este framework é indicado principalmente para:

- mini projetos de análise;
- datasets utilizados em cursos e trilhas de estudo;
- datasets públicos;
- estudos exploratórios;
- exercícios de SQL;
- análises com Python;
- análises em Excel ou Google Sheets;
- projetos rápidos em Power BI;
- prática de estatística aplicada;
- experimentação de novas técnicas analíticas.

Para projetos maiores, com maior necessidade de planejamento, documentação e aprofundamento, deve ser utilizado o **Framework de Análise de Dados completo**.

---

## Como usar o framework

O framework possui **três documentos**, mas eles têm funções diferentes. Para evitar dúvidas durante uma análise, use esta regra:

> **`framework-lite.md` = referência para pensar**
>
> **`template-analise-lite.md` = documento para preencher**
>
> **`checklist-projeto-curto.md` = verificação do projeto**

### Ordem de uso

A análise deve seguir a mesma ordem do processo analítico:

```text
1. Entender
      ↓
2. Perguntar
      ↓
3. Analisar
      ↓
4. Interpretar
      ↓
5. Concluir
```

E os documentos entram dessa forma:

| Momento | O que fazer | Documento | Ação |
|---|---|---|---|
| **Antes de começar** | Consultar o processo, as perguntas orientadoras e os princípios da análise | `framework-lite.md` | **Consultar** |
| **Entender** | Registrar contexto e entendimento dos dados | `template-analise-lite.md` | **Preencher** |
| **Perguntar** | Definir pergunta principal, perguntas analíticas e hipóteses | `template-analise-lite.md` | **Preencher** |
| **Analisar** | Executar as análises necessárias e registrar as evidências encontradas | `template-analise-lite.md` | **Preencher** |
| **Interpretar** | Explicar o significado dos resultados e transformar evidências em interpretações | `template-analise-lite.md` | **Preencher** |
| **Concluir** | Registrar conclusões, limitações e aprendizados | `template-analise-lite.md` | **Preencher** |
| **Final do projeto** | Verificar se as perguntas foram respondidas e se a análise está completa | `checklist-projeto-curto.md` | **Revisar** |

### Regra prática

Durante um projeto, pense nos documentos assim:

```text
                 REFERÊNCIA
                     │
                     ▼
          framework-lite.md
                     │
                     │ orienta
                     ▼
              ┌───────────────┐
              │    ANÁLISE    │
              └───────────────┘
                     │
                     ▼
       template-analise-lite.md
              (documento principal)
                     │
                     │ ao finalizar
                     ▼
        checklist-projeto-curto.md
              (verificação final)
```

### O papel de cada documento

#### `framework-lite.md`

É o **manual de referência**.

Use este documento para entender **como pensar e conduzir a análise**. Ele apresenta o processo completo e as perguntas que orientam cada etapa.

**Não é necessário preenchê-lo a cada projeto.**

#### `template-analise-lite.md`

É o **documento principal de trabalho**.

Crie ou copie uma versão desse template para cada análise e preencha ao longo do projeto. Ele concentra a documentação da análise, incluindo:

- contexto;
- entendimento dos dados;
- pergunta principal;
- perguntas analíticas;
- hipóteses;
- evidências;
- interpretações;
- conclusões;
- limitações;
- aprendizados.

**Este é o documento que você vai preencher.**

#### `checklist-projeto-curto.md`

É a **checagem final**.

Use-o depois de concluir a análise para verificar se o projeto possui evidências suficientes e se as perguntas propostas foram respondidas.

**Não substitui o template; serve para revisar o resultado final.**

### Fluxo recomendado

Na prática, o uso do framework pode ser resumido em:

```text
CONSULTAR
framework-lite.md
       ↓
PREENCHER
template-analise-lite.md
       ↓
EXECUTAR A ANÁLISE
SQL / Python / Excel / Power BI etc.
       ↓
ATUALIZAR O TEMPLATE
com evidências, interpretações e conclusões
       ↓
REVISAR
checklist-projeto-curto.md
       ↓
CONCLUIR O PROJETO
```

> **Regra para memorizar:** consulte o framework, preencha o template e revise com o checklist.

---

## Princípios

### 1. Começar pelo problema

A ferramenta não define a análise.

Primeiro é necessário entender o problema e formular as perguntas. Depois são escolhidas as técnicas e ferramentas adequadas.

### 2. Entender antes de analisar

Antes dos cálculos, é necessário compreender aspectos básicos dos dados:

- o que uma linha representa;
- qual é a granularidade;
- qual é a unidade de análise;
- quais são os fatos;
- quais são as dimensões;
- quais métricas são relevantes.

### 3. Analisar com propósito

Uma análise deve existir porque ajuda a responder uma pergunta.

Não é necessário criar gráficos, métricas ou cálculos apenas porque são possíveis.

### 4. Evidência não é conclusão

Encontrar um número ou padrão é apenas o começo.

O processo deve avançar de:

```text
Resultado
   ↓
Evidência
   ↓
Interpretação
   ↓
Conclusão
```

### 5. Saber quando parar

Um dataset pode permitir dezenas de análises diferentes.

Isso não significa que todas precisam ser realizadas.

> **O projeto termina quando as perguntas propostas foram respondidas com evidências suficientes.**

Novas perguntas podem originar novos projetos.

---

## Laboratório de Análises de Dados

Este framework foi desenvolvido principalmente para apoiar os projetos do repositório **`laboratorio-analises-de-dados`**.

O laboratório reúne projetos curtos utilizando diferentes abordagens, ferramentas e técnicas, como:

- SQL;
- Python;
- pandas;
- Excel;
- Google Sheets;
- Power BI;
- estatística descritiva;
- análise exploratória;
- análise temporal;
- segmentação;
- comparação;
- visualização de dados.

A intenção é aumentar a frequência com que o processo completo de análise é praticado, enquanto projetos médios e longos continuam sendo utilizados para desenvolver análises mais profundas e soluções end-to-end.

---

## Filosofia

Projetos curtos não significam análises incompletas.

O escopo pode ser pequeno enquanto o raciocínio permanece estruturado.

O objetivo deste framework é justamente encontrar esse equilíbrio:

> **menos documentação, menos complexidade e mais ciclos completos de análise.**

## Navegação no toolkit

- [Guia de referência](guias/framework-lite.md).
- [Template Markdown para preencher](templates/template-analise-lite.md).
- [Versão Word disponível no workspace](templates/template-analise-lite.docx), com campo adicional de processo de negócio.
- [Checklist final](checklists/checklist-projeto-curto.md).
- [Framework Completo](../completo/README.md), quando o escopo exigir maior profundidade.
- [Apoio compartilhado](../../compartilhado/README.md), consultado somente quando útil.

Copie o template para o repositório da análise; não preencha os documentos de referência deste toolkit. O Lite continua usando uma documentação principal e uma revisão final, sem exigir os templates de Analytics Engineering.

[Voltar à área de Análise de Dados](../README.md) ou ao [toolkit](../../README.md).
