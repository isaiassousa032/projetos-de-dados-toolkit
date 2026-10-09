---
tags:
  - investigação_analítica
---
[Análise de Dados MOC](../../README.md) , 



> Este documento define meu método padrão para conduzir análises de dados de forma estruturada, orientada a perguntas e focada em decisões.
>
> Ele deve ser utilizado **depois do diagnóstico inicial da base**, realizado com a nota [Guia de Primeiras Perguntas para um Novo Projeto de Dados](../../../compartilhado/guias/guia-primeiras-perguntas.md).

---

**MOC:** [Guias, Ajuda e Boas Práticas (MOC)](../README.md)  
**Pré-requisito:** [Guia de Primeiras Perguntas para um Novo Projeto de Dados](../../../compartilhado/guias/guia-primeiras-perguntas.md)

---

## 🧭 Onde este framework começa

Antes de iniciar este método, eu já devo ter uma compreensão mínima dos dados:

- o que uma linha representa;
- qual é a granularidade da base;
- qual é a unidade de análise desejada;
- quais são as chaves principais;
- qual período os dados cobrem;
- quais eventos ou fatos estão registrados;
- quais dimensões contextualizam esses fatos;
- quais métricas podem ser construídas;
- quais limitações e problemas de qualidade já são conhecidos.

> Se eu ainda não consigo responder a essas perguntas, devo voltar para [Guia de Primeiras Perguntas para um Novo Projeto de Dados](../../../compartilhado/guias/guia-primeiras-perguntas.md).

Este framework **não serve para descobrir o que existe na base**. Ele serve para transformar uma base já minimamente compreendida em **perguntas, evidências, insights e decisões**.

---

# 📌 Visão Geral do Método

O fluxo principal possui 6 etapas:

```text
Diagnóstico inicial dos dados
        │
        │  Guia de Primeiras Perguntas para um Novo Projeto de Dados
        ▼
┌──────────────────────────────┐
│ 1. Tradução do Problema      │
│ Pergunta aberta → fechada    │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 2. Decomposição Analítica    │
│ Pergunta → subperguntas      │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 3. Hipóteses e Priorização   │
│ Explicações a serem testadas │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 4. Validação e Evidências    │
│ SQL / Python / BI            │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 5. Síntese dos Insights      │
│ Evidência → interpretação    │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ 6. Recomendação e Decisão    │
│ Insight → ação               │
└──────────────────────────────┘
```

---

# 📜 Detalhamento das Etapas

## 1. Tradução do Problema — Pergunta Aberta → Pergunta Fechada

Demandas de negócio frequentemente chegam de forma vaga:

> “Por que as vendas caíram?”

> “O que está acontecendo com as internações?”

> “Como melhorar a retenção?”

Essas são **perguntas abertas**. Elas indicam um problema, mas ainda não determinam exatamente o que precisa ser medido ou comparado.

Meu primeiro trabalho como analista é transformar a pergunta aberta em uma pergunta que possa ser investigada com dados.

### Características de uma boa pergunta fechada

Ela deve ser:

- **específica** — deixa claro o fenômeno investigado;
- **mensurável** — pode ser respondida por métricas ou evidências;
- **delimitada** — possui período, população ou contexto quando necessário;
- **comparável** — permite observar diferenças, tendências ou desvios;
- **relevante** — sua resposta ajuda em alguma decisão.

### Exemplo

**Pergunta aberta:**

> Por que o faturamento caiu?

**Pergunta fechada:**

> Quais categorias, regiões e canais apresentaram maior contribuição para a queda de faturamento no último trimestre em comparação ao trimestre anterior?

### Teste rápido

> **Depois de ler a pergunta, consigo imaginar quais métricas, dimensões e comparações preciso utilizar para respondê-la?**

Se não, a pergunta provavelmente ainda está aberta demais.

---

## 2. Decomposição Analítica — Pergunta Principal → Subperguntas

Uma pergunta fechada ainda pode ser grande demais para ser respondida de uma única vez.

Por isso, devo quebrá-la em **perguntas analíticas menores**.

### Exemplo

Pergunta principal:

> Quais fatores explicam a queda de faturamento no último trimestre?

Subperguntas:

1. O número de pedidos diminuiu?
2. O ticket médio diminuiu?
3. A queda ocorreu em todas as regiões?
4. Quais categorias tiveram maior redução?
5. Algum canal apresentou comportamento diferente?
6. A queda está concentrada em algum período específico?
7. Houve perda de clientes ou redução da frequência de compra?

### Regra mental

Uma boa decomposição costuma explorar:

```text
Quanto mudou?
    ↓
Onde mudou?
    ↓
Quando mudou?
    ↓
Para quem mudou?
    ↓
Em qual produto/processo mudou?
    ↓
O que pode explicar a mudança?
```

### Métricas e dimensões entram aqui como ferramentas

Neste ponto, não preciso redescobrir a estrutura da base. Isso já foi feito no diagnóstico inicial.

Agora utilizo:

- **métricas** para quantificar o fenômeno;
- **dimensões** para segmentá-lo;
- **tempo** para observar evolução;
- **comparações** para dar significado aos números.

### Observação conceitual — Fatos e Dimensões

Um **fato** não deve ser entendido simplesmente como “uma coluna numérica central”.

Em termos analíticos e de modelagem, o fato normalmente representa um **evento ou processo observado em determinada granularidade**, como:

- uma venda;
- um item de pedido;
- uma internação;
- uma candidatura;
- uma sessão de uso;
- uma transação.

Esse evento pode possuir **várias medidas**, por exemplo:

```text
quantidade
valor_venda
desconto
custo
tempo_internacao
```

As **dimensões** fornecem contexto para analisar esses eventos:

```text
cliente
produto
região
canal
tempo
categoria
hospital
cargo
```

> **Fato = o que aconteceu.**  
> **Dimensão = sob qual contexto aconteceu.**  
> **Métrica = como vou quantificar o fenômeno.**

---

## 3. Formulação de Hipóteses e Priorização

Depois de decompor a pergunta, devo criar explicações plausíveis que possam ser testadas.

> **Uma hipótese não é uma conclusão antecipada. É uma possibilidade que será confrontada com os dados.**

### Estrutura simples

Uma hipótese analítica costuma combinar:

```text
Métrica + Dimensão + Comparação / Relação esperada
```

### Exemplo

> O faturamento dos clientes entre 40 e 50 anos é maior que o das demais faixas etárias.

- **Métrica:** faturamento;
- **Dimensão:** faixa etária;
- **Comparação:** 40–50 anos vs. demais faixas.

Outro exemplo:

> A queda de faturamento está concentrada no canal de vendas online.

- **Métrica:** faturamento;
- **Dimensão:** canal;
- **Comparação:** período atual vs. período anterior.

---

### Priorizar antes de analisar

Não preciso testar tudo o que é possível.

Para cada hipótese, pergunto:

1. Ela ajuda a responder a pergunta principal?
2. Tenho dados suficientes para testá-la?
3. O resultado pode mudar uma decisão?
4. A análise tem custo razoável em relação ao valor esperado?

### Filtro de acionabilidade

> **Se essa hipótese for confirmada ou refutada, alguém consegue tomar uma decisão diferente?**

- **SIM** → priorizar;
- **TALVEZ** → manter como secundária;
- **NÃO** → provavelmente é curiosidade analítica.

### Matriz de priorização

| ID | Hipótese | Relevância | Acionável? | Dados disponíveis? | Prioridade |
|---|---|---:|---:|---:|---:|
| H01 | | Alta | Sim | Sim | Alta |
| H02 | | Média | Sim | Sim | Média |
| H03 | | Baixa | Não | Sim | Baixa |

---

## 4. Validação Técnica e Registro de Evidências

Agora começa a investigação propriamente dita.

A ferramenta é secundária. O objetivo é produzir **evidência confiável** para responder às perguntas e testar as hipóteses.

Posso utilizar:

- SQL;
- Python / pandas;
- Power BI / DAX;
- Excel;
- outras ferramentas analíticas.

### Exemplo em SQL

```sql
SELECT
    faixa_etaria,
    SUM(valor_gasto) AS faturamento,
    AVG(valor_gasto) AS ticket_medio
FROM vendas
GROUP BY faixa_etaria
ORDER BY faturamento DESC;
```

### Exemplo em Python

```python
df.groupby("faixa_etaria")["valor_gasto"].agg(["sum", "mean"])
```

> Não devo criar uma query ou gráfico porque “parece interessante”. Cada análise deve existir para responder uma pergunta ou testar uma hipótese.

---

### Comparado a quê?

Um valor isolado costuma dizer pouco.

Sempre que fizer sentido, comparo o resultado com uma referência:

- período anterior;
- mesmo período do ano anterior;
- meta;
- média histórica;
- outro segmento;
- outra região;
- outra categoria;
- benchmark disponível.

Exemplo fraco:

> A receita foi de R$ 2 milhões.

Exemplo útil:

> A receita foi de R$ 2 milhões, queda de 18% em relação ao mês anterior.

---

### Matriz de evidências

| ID | Pergunta / Hipótese | Método | Resultado | Status | Evidência |
|---|---|---|---|---|---|
| H01 | Clientes <30 são os maiores compradores | Receita por faixa etária | 41–50 concentra maior receita | ❌ Refutada | Query / gráfico |
| H02 | App possui maior retenção que Web | Taxa de retenção por canal | App +25% | ✅ Confirmada | Query / gráfico |

### Status possíveis

- ✅ **Confirmada** — evidência consistente com a hipótese;
- ❌ **Refutada** — evidência contradiz a hipótese;
- ⚪ **Inconclusiva** — dados insuficientes ou resultado ambíguo;
- 🟡 **Parcialmente confirmada** — comportamento ocorre apenas em parte da população/período.

> **“Inconclusivo” também é um resultado válido.** Não devo forçar uma conclusão quando os dados não sustentam uma.

---

## 5. Evidência → Insight

Encontrar um número interessante ainda não significa ter encontrado um insight.

### Estrutura

```text
Dado
  ↓
Evidência
  ↓
Interpretação
  ↓
Insight
```

### Exemplo

**Dado:**

> Receita do canal online = R$ 720 mil.

**Evidência:**

> O canal online caiu 31% enquanto os demais canais permaneceram relativamente estáveis.

**Insight:**

> A queda geral de faturamento está concentrada no canal online, que explica a maior parte da redução observada no período.

### Perguntas para transformar evidência em insight

- O que mudou?
- Qual é o tamanho da mudança?
- Onde ela está concentrada?
- Isso é esperado ou anormal?
- Qual fator parece ter maior contribuição?
- Qual é a implicação para o problema inicial?

---

## 6. Insight → Recomendação → Decisão

O objetivo final da análise não é produzir gráficos.

É reduzir incerteza para apoiar uma decisão.

### Estrutura da síntese final

#### 1. Problema

> Qual pergunta precisávamos responder?

#### 2. Evidência principal

> O que os dados mostraram?

#### 3. Insight

> Como essa evidência deve ser interpretada?

#### 4. Recomendação

> O que deveria ser feito com base nisso?

#### 5. Próximo passo

> O que ainda precisa ser investigado, monitorado ou validado?

---

### Exemplo

**Problema**  
> Por que o faturamento caiu no último trimestre?

**Evidência**  
> 68% da redução absoluta está concentrada no canal online, principalmente na categoria Eletrônicos.

**Insight**  
> A queda não é generalizada; ela está concentrada em uma combinação específica de canal e categoria.

**Recomendação**  
> Priorizar a investigação do funil de vendas online de Eletrônicos antes de realizar ações amplas em todos os canais.

---

# 🛑 Critério de Parada da Análise

Uma análise não termina quando todas as possibilidades foram exploradas.

Ela termina quando existe evidência suficiente para responder a pergunta de negócio com o nível de confiança necessário.

### Posso encerrar quando:

- [ ] a pergunta principal está respondida;
- [ ] as subperguntas prioritárias foram investigadas;
- [ ] as hipóteses mais relevantes foram testadas;
- [ ] os principais drivers foram identificados;
- [ ] as limitações da conclusão estão claras;
- [ ] existe uma recomendação ou conclusão justificável;
- [ ] novas análises estão adicionando pouco valor à decisão.

### Sinal de alerta

> Se continuo criando gráficos apenas porque “ainda existem colunas para explorar”, provavelmente já saí da investigação orientada a problema e entrei em exploração sem objetivo.

---

# ⚠️ Diferenciar três coisas

## Achado

Algo observado nos dados.

> Clientes entre 41 e 50 anos representam 48% da receita.

## Insight

Interpretação relevante do achado dentro do problema analisado.

> A receita está fortemente concentrada em um segmento etário específico.

## Recomendação

Ação sugerida a partir do insight.

> Avaliar campanhas específicas para retenção desse segmento e investigar oportunidades de crescimento nos segmentos menos representados.

```text
Achado ≠ Insight ≠ Recomendação
```

---

# 🧠 Regra Mental do Framework

Quando estiver perdido durante uma análise, voltar para esta sequência:

```text
1. O que preciso responder?
        ↓
2. Em quais perguntas menores posso quebrar isso?
        ↓
3. Quais hipóteses explicariam o comportamento?
        ↓
4. Que evidência confirma ou refuta cada hipótese?
        ↓
5. O que essa evidência significa?
        ↓
6. Que decisão ela pode apoiar?
```

Ou, de forma resumida:

```text
PERGUNTA
   ↓
HIPÓTESE
   ↓
EVIDÊNCIA
   ↓
INSIGHT
   ↓
AÇÃO
```

---

# 🔄 Relação entre os dois documentos

Meu processo completo para novos projetos passa a ser:

```text
Novo dataset / nova fonte
        ↓
Guia de Primeiras Perguntas para um Novo Projeto de Dados
        ↓
Entender granularidade, chaves, período, fatos,
dimensões, métricas, qualidade e limitações
        ↓
────────────────────────────────────────────
        ↓
Método para as minhas análises
        ↓
Pergunta aberta → pergunta fechada
        ↓
Subperguntas
        ↓
Hipóteses
        ↓
Validação
        ↓
Evidências
        ↓
Insights
        ↓
Recomendações
        ↓
Decisão
```

### Responsabilidade de cada nota

| Documento | Pergunta central |
|---|---|
| [Guia de Primeiras Perguntas para um Novo Projeto de Dados](../../../compartilhado/guias/guia-primeiras-perguntas.md) | **“O que são estes dados e até onde posso confiar neles?”** |
| [Framework de Análise de Dados Do Problema à Tomada de Decisão](framework-analise-de-dados.md) | **“Como transformo esses dados em uma resposta útil?”** |

---

# 📝 Template de Nota de Análise para Obsidian

Use este template **depois que o diagnóstico inicial dos dados já estiver concluído**.

```markdown
---
tags:
  - analise-de-dados
  - projeto
status: em_andamento
data_inicio: {{date}}
area_negocio: ""
---

# 📊 Análise: [Nome do Projeto / Problema]

## 0. Referência do Diagnóstico Inicial

- **Diagnóstico da base:** Guia de Primeiras Perguntas para um Novo Projeto de Dados
- **Granularidade:**
- **Unidade de análise:**
- **Período:**
- **Principais métricas disponíveis:**
- **Principais dimensões disponíveis:**
- **Limitações relevantes:**

---

## 1. Problema de Negócio

### Pergunta aberta
>

### Pergunta fechada
>

### Decisão que esta análise deve apoiar
>

---

## 2. Perguntas Analíticas

1.
2.
3.
4.
5.

---

## 3. Hipóteses Priorizadas

| ID | Hipótese | Prioridade | Motivo |
|---|---|---|---|
| H01 | | Alta | |
| H02 | | Média | |
| H03 | | Baixa | |

---

## 4. Validação e Evidências

### H01 — [Hipótese]

- **Status:** ✅ Confirmada / ❌ Refutada / 🟡 Parcial / ⚪ Inconclusiva
- **Método:**
- **Comparação utilizada:**
- **Resultado:**
- **Evidência:**
- **Interpretação:**

### H02 — [Hipótese]

- **Status:**
- **Método:**
- **Comparação utilizada:**
- **Resultado:**
- **Evidência:**
- **Interpretação:**

---

## 5. Principais Insights

### Insight 1

**Evidência:**
>

**Interpretação:**
>

**Implicação:**
>

---

## 6. Síntese Executiva

### Problema
>

### Principais descobertas
-
-
-

### Recomendações
-
-
-

### Limitações
-
-

### Próximos passos
-
-

---

## 7. Critério de Encerramento

- [ ] Pergunta principal respondida
- [ ] Hipóteses prioritárias testadas
- [ ] Evidências registradas
- [ ] Insights sintetizados
- [ ] Limitações documentadas
- [ ] Recomendação ou conclusão formulada
```

---

# ✅ Checklist Rápido Durante uma Análise

Quando eu sentir que estou me perdendo, verificar:

- [ ] Estou tentando responder uma pergunta clara?
- [ ] Esta query/gráfico responde alguma pergunta ou hipótese?
- [ ] Estou usando a granularidade correta?
- [ ] A métrica está sendo agregada corretamente?
- [ ] Tenho uma comparação que dê contexto ao número?
- [ ] Estou distinguindo correlação, associação e causalidade?
- [ ] Estou registrando resultados que refutam minhas hipóteses?
- [ ] Estou diferenciando achado de insight?
- [ ] O insight tem relação com o problema original?
- [ ] A recomendação é realmente sustentada pelos dados?
- [ ] Já tenho evidência suficiente para parar?

---

# 🎯 Princípio Central

> **Não analisar dados para descobrir tudo o que existe neles.**  
> **Analisar dados para reduzir a incerteza sobre uma pergunta importante.**

A ferramenta vem depois.

```text
Problema → Pergunta → Hipótese → Evidência → Insight → Decisão
```

## Nota técnica sobre os exemplos

As consultas e os números deste guia ilustram o raciocínio e não representam resultados verificados. O exemplo de `AVG(valor_gasto)` como ticket médio pressupõe uma linha por pedido elegível. Em uma base de itens, calcule receita elegível dividida por pedidos distintos elegíveis. Declare e valide o grão antes de reutilizar a consulta; consulte a [ficha de métrica](../../../analytics-engineering/templates/definicao-metricas-negocio.md).

[Voltar ao Framework Completo](../README.md).
