# Framework de Análise de Dados — Lite

> Método enxuto para conduzir projetos curtos de análise de dados, com duração aproximada de **1 a 5 dias**.

O objetivo deste framework não é documentar cada etapa em detalhes, mas garantir que uma análise curta tenha **problema, raciocínio, evidências e conclusão**.

## Fluxo

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

## 1. Entender — O que são estes dados?

Antes de começar a analisar, preciso entender minimamente a base.

### Problema

- O que quero descobrir?
- Qual é o contexto?
- Existe alguma decisão ou situação que esta análise pode ajudar a compreender?

### Estrutura dos dados

Complete:

**Cada linha representa:**  
`____________________________`

**Período dos dados:**  
`____________________________`

**Granularidade dos dados:**  
`____________________________`

**Unidade que quero analisar:**  
`____________________________`

### Fatos, dimensões e métricas

Identifique apenas o que for relevante para a análise.

**Fatos / eventos:**
- 
- 

**Dimensões:**
- 
- 
- 

**Métricas principais:**
- 
- 
- 

### Qualidade

Faça uma verificação rápida de:

- valores ausentes;
- duplicatas;
- tipos incorretos;
- valores impossíveis ou suspeitos;
- outliers relevantes;
- limitações conhecidas.

> Não preciso corrigir tudo. Preciso saber se os problemas encontrados afetam a análise que quero realizar.

---

## 2. Perguntar — O que quero responder?

Defina uma pergunta principal.

> **Pergunta principal:**  
> _______________________________________________

Depois, decomponha em aproximadamente **3 a 5 perguntas menores**.

1. 
2. 
3. 
4. 
5. 

As perguntas podem explorar:

```text
Quanto?
Onde?
Quando?
Quem?
Qual grupo?
Comparado a quê?
O que pode explicar?
```

### Hipóteses

Quando fizer sentido, registre o que espera encontrar **antes de verificar os resultados**.

- H1:
- H2:
- H3:

> Hipóteses são possibilidades a serem testadas, não conclusões antecipadas.

---

## 3. Analisar — O que os dados mostram?

Escolha as técnicas necessárias para responder às perguntas.

Podem incluir:

- estatística descritiva;
- agregações;
- segmentações;
- comparações;
- análise temporal;
- distribuições;
- correlações;
- rankings;
- análise de outliers;
- visualizações;
- outras técnicas adequadas ao problema.

Para cada análise, mantenha a lógica:

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

> Não adicionar análises apenas porque são possíveis.

---

## 4. Interpretar — O que isso significa?

Transforme resultados em evidências e evidências em insights.

Evite apenas registrar:

> "A categoria A possui 35% das vendas."

Pergunte:

> **E daí? O que esse resultado ajuda a entender?**

Para os principais achados, utilize:

**Evidência:**  
O que os dados mostraram?

**Interpretação:**  
O que isso significa dentro do problema analisado?

**Implicação:**  
Por que isso importa?

---

## 5. Concluir — O que aprendi?

Ao final, responda novamente à pergunta principal.

### Principais conclusões

1. 
2. 
3. 

### Limitações

- 
- 

### Próximos passos

Somente quando realmente necessários:

- 
- 

---

# Critério de encerramento

O projeto não precisa explorar todas as possibilidades do dataset.

> **A análise termina quando as perguntas propostas foram respondidas com evidências suficientes.**

Se novas perguntas surgirem, elas podem virar outro projeto.

---

# Princípio do Framework Lite

> **Pequeno no escopo, completo no raciocínio.**

O objetivo de um projeto curto não é demonstrar complexidade.

É praticar repetidamente o processo de transformar:

**dados → perguntas → análise → evidências → conclusões.**