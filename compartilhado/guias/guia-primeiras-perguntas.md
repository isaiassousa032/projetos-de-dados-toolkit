---
tags:
  - diagnostico_inicial
---
MOC: [Análise de Dados MOC](../../analise-de-dados/README.md)

**“O que são estes dados e até onde posso confiar neles?”**


> Este guia deve ser utilizado **antes de iniciar a análise exploratória, escrever queries complexas ou construir dashboards**.


> O objetivo é entender **o problema, os dados e sua estrutura** antes de tentar encontrar respostas.

---
## 🧠 1. Qual problema estou tentando resolver?

Antes de olhar para gráficos ou métricas:
- Qual é o **contexto do projeto**?
- Qual problema motivou esta análise?
- Quem é o **stakeholder**?
- Que decisão essa pessoa precisa tomar?
- O que seria uma resposta útil para ela?
### Pergunta aberta

> Qual é a pergunta original?

**Exemplo:**
> Por que nossas vendas estão ruins?

### Pergunta fechada

Transforme a pergunta aberta em algo:
- específico;
- mensurável;
- analisável;
- limitado no tempo ou contexto.

**Exemplo:**
> Quais categorias, regiões e canais tiveram maior queda de faturamento no último trimestre em comparação ao trimestre anterior?

### Teste rápido

> **Consigo imaginar quais dados seriam necessários para responder essa pergunta?**

Se não, a pergunta provavelmente ainda está aberta demais.

---

# 🔎 2. O que uma linha representa?

Esta é uma das perguntas mais importantes de todo projeto.

> **Qual é a granularidade dos dados?**

Complete:
> **Cada linha representa ____________.**

Exemplos:
- uma venda;
- um pedido;
- um produto dentro de um pedido;
- um cliente;
- uma internação hospitalar;
- uma vaga de emprego;
- uma avaliação;
- uma medição diária.
### Exemplo

Em uma tabela:

|order_id|product_id|quantity|price|
|---|---|---|---|
|1001|A|2|50|
|1001|B|1|80|

A granularidade não é:

> Pedido.

É:

> **Produto dentro de um pedido.**

Isso significa que `order_id` pode aparecer várias vezes.

---

# 🔑 3. Qual é a chave da tabela?

Pergunte:

- Existe uma coluna que identifica cada linha?
- A chave é única?
- Preciso combinar duas ou mais colunas?
- Existem registros duplicados?

Exemplos:
```
customer_id
```

ou:
```
order_id + product_id
```

### Registre

**Chave primária ou identificador esperado:**
```

```

**A chave é realmente única?**

```
Sim / Não / Ainda não verificado
```

---

# 📅 4. Qual é o período dos dados?

Identifique:
- menor data;
- maior data;
- frequência dos registros;
- existência de períodos ausentes.

### Registre

**Período disponível:**
```
____/____/____ até ____/____/____
```

**Granularidade temporal:**
```
Hora / Dia / Semana / Mês / Outro
```

Pergunte também:

> O período disponível é suficiente para responder a pergunta de negócio?

---

# 🎯 5. Qual é a unidade de análise?

A granularidade da tabela e a unidade da análise podem ser diferentes.

Por exemplo:

**Granularidade dos dados**
> Produto dentro de um pedido.

**Unidade da análise**
> Cliente.

Nesse caso, será necessário agregar os dados antes de analisar clientes.

### Complete

> **Os dados estão no nível de:** __________

> **Mas quero analisar no nível de:** __________

---

# 📊 6. Quais são os Fatos?

Fatos são eventos, valores ou métricas que podem ser analisados quantitativamente.

Pergunte:

> **O que aconteceu?**

Exemplos:

```
quantidade
valor_venda
receita
custo
desconto
tempo_internacao
numero_pedidos
morte
avaliacao
```

### Fatos encontrados

```
-
-
-
```

---

# 🧩 7. Quais são as Dimensões?

Dimensões respondem perguntas como:

> **Quem? O quê? Onde? Quando? Como?**

Separe-as por contexto.

### 👤 Pessoa / Cliente

```
idade
sexo
cliente
segmento
profissão
```

### 📦 Produto / Serviço

```
produto
categoria
marca
tipo_servico
```

### 🌎 Localização

```
cidade
estado
região
país
bairro
```

### 📅 Tempo

```
data
ano
mês
dia_da_semana
trimestre
```

### ⚙️ Processo / Operação

```
canal
status
tipo_atendimento
modalidade
origem
```

---

# 🔗 8. Existem várias tabelas?

Se houver mais de uma tabela:

- Qual é a granularidade de cada uma?
    
- Qual é a chave primária de cada tabela?
    
- Quais são as chaves estrangeiras?
    
- Como as tabelas se relacionam?
    

### Exemplo

```
customers
    customer_id
        │
        │ 1:N
        ▼
orders
    order_id
    customer_id
        │
        │ 1:N
        ▼
order_items
    order_id
    product_id
```

Pergunte:

> **O relacionamento é realmente 1 ou existem duplicações inesperadas criando N?**

---

# 🏗️ 9. Qual seria a estrutura Fato × Dimensão?

Se o projeto for para BI ou modelagem dimensional, tente imaginar:

```
            Dim_Cliente
                 │
                 │
Dim_Produto ── Fato_Vendas ── Dim_Data
                 │
                 │
             Dim_Região
```

### Tabela fato candidata

```

```

### Dimensões candidatas

```
-
-
-
-
```

> Não é necessário construir um modelo estrela imediatamente.  
> O objetivo neste momento é apenas **entender conceitualmente a estrutura dos dados**.

---

# 🧮 10. Quais métricas realmente importam?

Não comece criando dezenas de medidas.

Pergunte:

> **Quais números respondem diretamente à pergunta do projeto?**

### Métricas principais

```
-
-
-
```

### Métricas secundárias

```
-
-
-
```

Exemplos:

```
Receita
Ticket médio
Quantidade de pedidos
Clientes ativos
Taxa de conversão
Mortalidade
Tempo médio de internação
```

---

# ⚠️ 11. Como essas métricas devem ser agregadas?

Nem toda coluna numérica deve ser somada.

Pergunte:

|   |   |
|---|---|
|Métrica|Agregação|
|Receita|SUM|
|Quantidade|SUM|
|Preço|AVG / MEDIAN|
|Cliente|DISTINCTCOUNT|
|Pedido|DISTINCTCOUNT|
|Taxa|Cálculo específico|

Cuidado principalmente com:

```
IDs
percentuais
médias
taxas
estoques
saldos
valores acumulados
```

> **Número não significa automaticamente métrica somável.**

---

# 🧹 12. Os dados parecem confiáveis?

Antes da análise profunda, faça um diagnóstico básico.

### Estrutura

- Quantas linhas existem?
    
- Quantas colunas existem?
    
- Os tipos estão corretos?
    
- Existem colunas completamente vazias?
    

### Nulos

- Quais colunas possuem valores ausentes?
    
- Qual percentual está ausente?
    
- O nulo significa dado faltante ou ausência real?
    

### Duplicados

- Existem linhas duplicadas?
    
- Existem IDs duplicados que deveriam ser únicos?
    

### Valores impossíveis

Procure coisas como:

```
idade = -5
preço = -100
data futura inesperada
quantidade = 0
percentual = 350%
```

---

# 🗂️ 13. O que cada coluna significa?

Nunca presuma que entende uma coluna apenas pelo nome.

Exemplo:

```
VAL_TOT
```

Pode significar:

- valor total faturado;
    
- valor total aprovado;
    
- valor total solicitado;
    
- valor total pago.
    

São conceitos diferentes.

Para colunas importantes, registre:

|   |   |   |   |
|---|---|---|---|
|Coluna|Significado|Tipo|Observação|
|||||
|||||
|||||

Se houver documentação oficial, utilize-a como fonte de verdade.

---

# 🔄 14. Existem colunas derivadas?

Pergunte:

> Essa informação veio diretamente da fonte ou foi calculada?

Exemplos:

```
idade
faixa_etaria
ticket_medio
receita_estimada
tempo_internacao
margem
```

Registre as regras importantes.

```
margem = receita - custo
```

---

# 🧪 15. Quais hipóteses posso testar?

Agora que os dados são compreendidos, transforme a pergunta principal em pequenas hipóteses.

Estrutura útil:

> **Fato + Dimensão + Comparação**

Exemplo:

> O faturamento de clientes entre 40 e 50 anos é maior que o das demais faixas etárias.

### Hipóteses

- **H01:**
    
- **H02:**
    
- **H03:**
    
- **H04:**
    
- **H05:**
    

---

# 🎯 16. Essa análise pode gerar alguma ação?

Para cada pergunta ou hipótese, pergunte:

> **Se eu descobrir a resposta, alguém consegue tomar uma decisão diferente?**

### Se SIM

Continue investigando.

### Se NÃO

Provavelmente é apenas:

> **curiosidade analítica.**

Ela pode ser interessante, mas não deve necessariamente receber prioridade.

---

# 🧭 17. Quais são minhas perguntas analíticas?

A pergunta principal normalmente se transforma em perguntas menores.

Exemplo:

### Pergunta principal

> Quais fatores estão relacionados à queda de faturamento?

### Perguntas analíticas

1. A queda ocorreu em todas as regiões?
    
2. Quais categorias tiveram maior redução?
    
3. Houve redução no número de clientes?
    
4. O ticket médio diminuiu?
    
5. Algum canal apresentou comportamento diferente?
    
6. A mudança está concentrada em algum período?
    

---

# 📐 18. Qual comparação faz sentido?

Um número sozinho geralmente significa pouco.

Pergunte:

> **Comparado a quê?**

Possíveis comparações:

```
período anterior
mesmo período do ano anterior
média histórica
meta
benchmark
outra região
outro segmento
outra categoria
```

Exemplo ruim:

> Receita de agosto foi R$ 2 milhões.

Exemplo melhor:

> Receita de agosto foi R$ 2 milhões, uma queda de 18% em relação a julho.

---

# 🚧 19. Quais são as limitações dos dados?

Registre problemas que podem afetar sua conclusão.

Exemplos:

```
Dados disponíveis apenas para São Paulo.

Período cobre somente 6 meses.

15% dos registros não possuem informação de categoria.

Receita é estimada, não observada.

Dados representam anúncios publicados, não necessariamente contratações realizadas.
```

Isso evita transformar:

> **evidência limitada**

em:

> **conclusão absoluta.**

---

# 🛑 20. Quando devo parar a análise?

Antes de começar, defina o critério de parada.

Pergunte:

> **O que preciso descobrir para considerar a pergunta respondida?**

Pare quando:

- as principais hipóteses tiverem sido testadas;
    
- a pergunta de negócio estiver respondida;
    
- os principais drivers estiverem identificados;
    
- novas análises estiverem gerando apenas curiosidades marginais.
    

> Análise não termina quando todas as possibilidades acabam.  
> Ela termina quando existe evidência suficiente para responder à pergunta.

---

# ✅ Checklist rápido — Antes de começar a analisar

Se eu conseguir responder estas perguntas, estou pronto para avançar:

- Qual problema quero resolver?
    
- Qual é a pergunta aberta?
    
- Qual é a pergunta fechada?
    
- Quem usará essa análise?
    
- Qual decisão essa análise deve apoiar?
    
- O que representa uma linha?
    
- Qual é a granularidade dos dados?
    
- Qual é a unidade da análise?
    
- Qual é a chave da tabela?
    
- Qual período os dados cobrem?
    
- Quais são os principais fatos?
    
- Quais são as principais dimensões?
    
- Como as tabelas se relacionam?
    
- Quais métricas realmente importam?
    
- Como cada métrica deve ser agregada?
    
- Existem nulos importantes?
    
- Existem duplicações?
    
- Existem valores impossíveis?
    
- Entendo o significado das principais colunas?
    
- Quais são as minhas hipóteses?
    
- Com o que vou comparar os resultados?
    
- Quais são as limitações dos dados?
    
- Sei quando considerar a análise concluída?
    

---

# 🧠 Regra mental

Ao receber qualquer dataset novo, pense nesta ordem:

```
1. Por quê?
   ↓
Qual problema quero resolver?

2. O quê?
   ↓
O que uma linha representa?

3. Quem / Onde / Quando / Como?
   ↓
Quais são as dimensões?

4. Quanto?
   ↓
Quais são os fatos e métricas?

5. Comparado a quê?
   ↓
Qual referência torna o número significativo?

6. Por quê?
   ↓
Quais hipóteses podem explicar o comportamento?

7. E daí?
   ↓
Que decisão pode ser tomada com essa descoberta?
```

---

# 🔗 Relação com o Framework de Análise

Este guia deve ser utilizado **antes e durante a etapa inicial do Framework de Análise de Dados**.

Fluxo recomendado:

```
Dataset / Problema
        ↓
Primeiras Perguntas
        ↓
Entendimento da Granularidade
        ↓
Qualidade e Estrutura dos Dados
        ↓
Fatos × Dimensões
        ↓
Pergunta Aberta → Pergunta Fechada
        ↓
Hipóteses
        ↓
SQL / Python / Power BI
        ↓
Evidências
        ↓
Insights
        ↓
Recomendação
        ↓
Decisão
```

> **Não comece pela ferramenta. Comece entendendo o que os dados representam e qual pergunta eles precisam responder.**

## Notas técnicas para reutilização

O conteúdo original acima usa fatos também no sentido amplo de valores observados. Em modelagem dimensional, declare o fato como evento ou estado de um processo no grão definido e diferencie suas medidas e métricas derivadas. Consulte [modelagem de dados](../../analytics-engineering/guias/modelagem-de-dados.md).

Os exemplos de `order_id + product_id` dependem da regra de origem: se um produto puder repetir dentro do mesmo pedido, essa combinação não identifica o item. Verifique `item_id`, posição estável ou outros atributos necessários antes de assumir unicidade.

[Voltar aos materiais compartilhados](../README.md).
