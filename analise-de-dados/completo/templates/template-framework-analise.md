# Template do Framework de Análise de Dados: Do Problema à Tomada de Decisão

**Use este documento depois do diagnóstico inicial da base.** Ele organiza a investigação desde a tradução do problema até a recomendação final, evitando análises sem direção.

Fluxo do método: Problema → Pergunta → Subperguntas → Hipóteses → Evidências → Insights → Recomendações → Decisão

## Identificação do projeto

| Campo                      | Preenchimento |
|--------------------------------|-------------------|
| **Nome do projeto**            |                   |
| **Data de início**             |                   |
| **Área / domínio**             |                   |
| **Stakeholder / público-alvo** |                   |
| **Fonte principal dos dados**  |                   |
| **Responsável pela análise**   |                   |

## 0. Pré-requisito: diagnóstico inicial concluído

Antes de usar este framework, confirme que você já entendeu minimamente a base: granularidade, unidade de análise, chaves, período, fatos/eventos, dimensões, métricas e limitações conhecidas.

- [ ] Sei o que uma linha representa.
- [ ] Conheço a granularidade atual e a unidade de análise desejada.
- [ ] Conheço as chaves e principais relacionamentos.
- [ ] Conheço o período coberto pelos dados.
- [ ] Mapeei fatos/eventos, dimensões e métricas relevantes.
- [ ] Registrei problemas de qualidade e limitações importantes.

**Principais restrições herdadas do diagnóstico inicial:**

[preencha]

## 1. Tradução do problema — Pergunta aberta → Pergunta fechada

**Contexto do problema:** *O que está acontecendo e por que esta análise existe?*

[preencha]

**Pergunta aberta recebida:**

[preencha]

**Pergunta fechada:** *Torne-a específica, mensurável, delimitada, comparável e relevante.*

[preencha]

**Decisão que precisa ser apoiada:**

[preencha]

**Métrica(s) principal(is) que representam o fenômeno:**

[preencha]

**Dimensões mais importantes para contextualizar o fenômeno:**

[preencha]

**Comparação principal:** *Ex.: período anterior, meta, segmento, região, benchmark.*

[preencha]

### Teste da pergunta fechada

- [ ] A pergunta é específica?
- [ ] É mensurável com os dados disponíveis?
- [ ] Possui período, população ou contexto quando necessário?
- [ ] Permite comparação ou identificação de desvio/tendência?
- [ ] A resposta pode influenciar uma decisão?

## 2. Decomposição analítica — Pergunta principal → Subperguntas

Quebre a pergunta principal em partes menores. Uma decomposição útil costuma explorar: Quanto mudou? Onde? Quando? Para quem? Em qual produto/processo? O que pode explicar?

| ID | Subpergunta analítica | Métrica | Dimensão | Comparação / corte | Prioridade |
|--------|---------------------------|-------------|--------------|------------------------|----------------|
| P01    |                           |             |              |                        |                |
| P02    |                           |             |              |                        |                |
| P03    |                           |             |              |                        |                |
| P04    |                           |             |              |                        |                |
| P05    |                           |             |              |                        |                |
| P06    |                           |             |              |                        |                |
| P07    |                           |             |              |                        |                |
| P08    |                           |             |              |                        |                |

**Sequência lógica da investigação:** *Ex.: volume → ticket → região → categoria → canal → período.*

[preencha]

## 3. Formulação de hipóteses e priorização

Hipótese = possibilidade a ser testada, não conclusão antecipada. Estrutura útil: Métrica + Dimensão + Comparação / relação esperada.

| ID | Hipótese | Relevância | Acionável? | Dados suficientes? | Custo | Prioridade |
|--------|--------------|----------------|----------------|------------------------|-----------|----------------|
| H01    |              |                |                |                        |           |                |
| H02    |              |                |                |                        |           |                |
| H03    |              |                |                |                        |           |                |
| H04    |              |                |                |                        |           |                |
| H05    |              |                |                |                        |           |                |
| H06    |              |                |                |                        |           |                |
| H07    |              |                |                |                        |           |                |
| H08    |              |                |                |                        |           |                |

**Hipóteses descartadas e motivo:**

[preencha]

## 4. Validação técnica e registro de evidências

Cada query, cálculo ou gráfico deve responder uma pergunta ou testar uma hipótese. A ferramenta é secundária; o objetivo é produzir evidência confiável.

| ID | Pergunta / hipótese | Método / análise | Resultado | Status | Evidência / referência |
|--------|-------------------------|----------------------|---------------|------------|----------------------------|
| E01    |                         |                      |               |            |                            |
| E02    |                         |                      |               |            |                            |
| E03    |                         |                      |               |            |                            |
| E04    |                         |                      |               |            |                            |
| E05    |                         |                      |               |            |                            |
| E06    |                         |                      |               |            |                            |
| E07    |                         |                      |               |            |                            |
| E08    |                         |                      |               |            |                            |
| E09    |                         |                      |               |            |                            |
| E10    |                         |                      |               |            |                            |

### Status permitidos

- [ ] Confirmada
- [ ] Refutada
- [ ] Parcialmente confirmada
- [ ] Inconclusiva

**Comparações utilizadas na análise:**

[preencha]

**Validações adicionais realizadas:** *Ex.: sanity checks, totais, reconciliação entre ferramentas, filtros, amostras.*

[preencha]

**Resultados inconclusivos e por quê:**

[preencha]

## 5. Evidência → Insight

Achado é algo observado. Insight é a interpretação relevante do achado dentro do problema analisado.

| ID | Evidência / achado | Interpretação | Insight | Impacto no problema |
|--------|------------------------|-------------------|-------------|-------------------------|
| I01    |                        |                   |             |                         |
| I02    |                        |                   |             |                         |
| I03    |                        |                   |             |                         |
| I04    |                        |                   |             |                         |
| I05    |                        |                   |             |                         |
| I06    |                        |                   |             |                         |
| I07    |                        |                   |             |                         |
| I08    |                        |                   |             |                         |

### Perguntas para validar cada insight

- [ ] O que mudou?
- [ ] Qual é o tamanho da mudança?
- [ ] Onde a mudança está concentrada?
- [ ] É esperado ou anormal?
- [ ] Qual fator parece ter maior contribuição?
- [ ] Qual é a implicação para a pergunta inicial?

## 6. Insight → Recomendação → Decisão

| ID | Insight | Recomendação | Responsável / área | Prioridade | Próximo passo |
|--------|-------------|------------------|------------------------|----------------|-------------------|
| R01    |             |                  |                        |                |                   |
| R02    |             |                  |                        |                |                   |
| R03    |             |                  |                        |                |                   |
| R04    |             |                  |                        |                |                   |
| R05    |             |                  |                        |                |                   |
| R06    |             |                  |                        |                |                   |

**Decisão recomendada:**

[preencha]

**O que deve ser feito primeiro?**

[preencha]

**O que não deve ser feito com base nesta análise?**

[preencha]

**O que ainda precisa ser investigado ou monitorado?**

[preencha]

## 7. Síntese executiva

**Problema:** *Qual pergunta precisávamos responder?*

[preencha]

**Evidência principal:** *O que os dados mostraram de mais importante?*

[preencha]

**Insight principal:** *Como essa evidência deve ser interpretada?*

[preencha]

**Recomendação principal:** *O que deveria ser feito com base nisso?*

[preencha]

**Próximo passo:**

[preencha]

**Limitações da conclusão:**

[preencha]

## 8. Critério de parada da análise

- [ ] A pergunta principal está respondida.
- [ ] As subperguntas prioritárias foram investigadas.
- [ ] As hipóteses mais relevantes foram testadas.
- [ ] Os principais drivers foram identificados.
- [ ] As limitações da conclusão estão claras.
- [ ] Existe uma recomendação ou conclusão justificável.
- [ ] Novas análises estão adicionando pouco valor à decisão.

**Motivo pelo qual considero a análise concluída:**

[preencha]

**Perguntas que ficaram para uma próxima versão:**

[preencha]

## 9. Controle de qualidade da conclusão

Mantenha a distinção: Achado ≠ Insight ≠ Recomendação.

| Tipo                   | Registro final |
|----------------------------|--------------------|
| **Achado principal**       |                    |
| **Insight principal**      |                    |
| **Recomendação principal** |                    |

- [ ] Minha recomendação está sustentada por evidência?
- [ ] Evitei tratar correlação como causalidade sem evidência?
- [ ] Evitei generalizar além do período/população analisados?
- [ ] As limitações estão explícitas?
- [ ] Consigo explicar a análise sem depender dos gráficos?
- [ ] A recomendação responde ao problema original?

## 10. Resumo final do projeto — 1 página

| Pergunta                                          | Resposta resumida |
|-------------------------------------------------------|-----------------------|
| **Qual problema foi analisado?**                      |                       |
| **Qual foi a pergunta fechada?**                      |                       |
| **Quais foram as 3 subperguntas mais importantes?**   |                       |
| **Quais hipóteses foram decisivas?**                  |                       |
| **Qual foi a evidência principal?**                   |                       |
| **Qual foi o insight principal?**                     |                       |
| **Qual recomendação foi gerada?**                     |                       |
| **Quais limitações precisam ser lembradas?**          |                       |
| **Qual decisão ou próximo passo este projeto apoia?** |                       |

**Regra mental:** O que preciso responder? → Em quais perguntas menores? → Quais hipóteses? → Que evidência? → O que significa? → Que decisão apoia?
