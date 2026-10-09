# Checklist — Projeto de Análise de Dados Lite

Checklist para revisar um projeto curto antes de considerá-lo concluído.

> **Regra:** o checklist é usado no final. O documento principal da análise é o `template-analise-lite.md`, e o `framework-lite.md` é a referência para conduzir o processo.

---

## 1. Entender

### Problema e contexto

- [ ] O contexto da análise está claro?
- [ ] Sei o que quero descobrir?
- [ ] Existe uma situação, problema ou decisão relacionada à análise?

### Estrutura dos dados

- [ ] Sei o que cada linha representa?
- [ ] Sei qual é o período dos dados?
- [ ] Entendi a granularidade?
- [ ] Defini a unidade de análise?
- [ ] Identifiquei os fatos/eventos relevantes?
- [ ] Identifiquei as dimensões relevantes?
- [ ] Identifiquei as métricas principais?

### Qualidade dos dados

- [ ] Verifiquei valores ausentes?
- [ ] Verifiquei duplicatas?
- [ ] Verifiquei tipos incorretos?
- [ ] Verifiquei valores impossíveis ou suspeitos?
- [ ] Verifiquei outliers relevantes?
- [ ] Registrei limitações que podem afetar a análise?

> Não é necessário corrigir todos os problemas encontrados. É necessário saber se eles afetam as perguntas que estão sendo respondidas.

---

## 2. Perguntar

- [ ] Existe uma pergunta principal claramente definida?
- [ ] A pergunta principal pode ser respondida pelos dados disponíveis?
- [ ] Tenho aproximadamente 3 a 5 perguntas analíticas?
- [ ] As perguntas ajudam a decompor a pergunta principal?
- [ ] Registrei hipóteses quando fizer sentido?
- [ ] As hipóteses foram definidas antes de verificar os resultados?

Perguntas úteis para revisar:

```text
Quanto?
Onde?
Quando?
Quem?
Qual grupo?
Comparado a quê?
O que pode explicar?
```

---

## 3. Analisar

Para cada análise realizada:

- [ ] Existe uma pergunta que justifica a análise?
- [ ] Escolhi uma métrica adequada?
- [ ] Escolhi dimensões/segmentações relevantes?
- [ ] Existe alguma comparação útil?
- [ ] A análise realmente ajuda a responder uma das perguntas?
- [ ] Registrei a evidência encontrada?

Fluxo esperado:

```text
Pergunta
   ↓
Métrica
   ↓
Dimensão / Segmentação
   ↓
Comparação
   ↓
Evidência
```

### Evitar

- [ ] Não criei análises, métricas ou gráficos apenas porque eram possíveis?
- [ ] Não aumentei o escopo sem necessidade?

---

## 4. Interpretar

Para os principais achados:

- [ ] Está claro o que os dados mostraram?
- [ ] Transformei o resultado em uma evidência relevante?
- [ ] Expliquei o que a evidência significa dentro do problema?
- [ ] Expliquei por que o achado importa?
- [ ] Diferenciei claramente resultado, evidência e interpretação?
- [ ] Evitei tratar hipótese como conclusão sem evidência?

Fluxo esperado:

```text
Resultado
   ↓
Evidência
   ↓
Interpretação
   ↓
Implicação
```

---

## 5. Concluir

- [ ] Registrei as principais descobertas?
- [ ] Respondi diretamente à pergunta principal?
- [ ] As conclusões são sustentadas pelas evidências encontradas?
- [ ] Registrei as limitações relevantes?
- [ ] Registrei próximos passos somente quando necessários?
- [ ] Registrei o que pratiquei e o principal aprendizado?

### Critério de encerramento

- [ ] As perguntas propostas foram respondidas com evidências suficientes?
- [ ] Novas descobertas não exigem ampliar o escopo deste projeto?

> **O projeto termina quando as perguntas propostas foram respondidas com evidências suficientes.**

Novas perguntas podem virar novos projetos.

---

# Revisão final

### Documentação

- [ ] O `template-analise-lite.md` está preenchido?
- [ ] As evidências e interpretações estão registradas?
- [ ] As conclusões estão registradas?
- [ ] As limitações estão registradas?

### Processo

- [ ] Segui a sequência **Entender → Perguntar → Analisar → Interpretar → Concluir**?
- [ ] Usei o `framework-lite.md` como referência quando necessário?
- [ ] Evitei complexidade ou documentação desnecessária?

### Resultado

- [ ] Consigo explicar o problema em poucas frases?
- [ ] Consigo explicar como cheguei às principais conclusões?
- [ ] Consigo apontar quais evidências sustentam cada conclusão?
- [ ] O projeto está pequeno no escopo, mas completo no raciocínio?

---

## Status do projeto

**Status:** [ ] Em andamento  [ ] Concluído  [ ] Precisa de revisão

**Data da revisão:**  
[AAAA-MM-DD]

**Observações finais:**

> [...]
