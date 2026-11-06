# Template de Diagnóstico Inicial para Projetos de Dados

**Use este documento antes da análise exploratória, queries complexas ou dashboards.** O objetivo é entender o problema, a granularidade, a estrutura e a confiabilidade dos dados antes de investigar hipóteses.

## Identificação do projeto

| Campo                       | Preenchimento |
|---------------------------------|-------------------|
| **Nome do projeto**             |                   |
| **Data de início**              |                   |
| **Fonte dos dados**             |                   |
| **Área / domínio**              |                   |
| **Stakeholder ou público-alvo** |                   |
| **Responsável**                 |                   |

## 1. Problema e objetivo

**Contexto do projeto:** *O que motivou a análise?*

[preencha]

**Pergunta aberta:** *Como o problema chegou até você?*

[preencha]

**Pergunta fechada:** *Torne-a específica, mensurável e analisável.*

[preencha]

**Decisão que a análise deve apoiar:**

[preencha]

**O que seria uma resposta útil ao final do projeto?**

[preencha]

### Teste rápido

- [ ] Consigo dizer claramente qual problema estou tentando resolver?
- [ ] Consigo explicar quais dados seriam necessários para responder à pergunta?
- [ ] A pergunta fechada tem escopo suficiente para orientar a análise?

## 2. Granularidade e unidade de análise

**O que uma linha representa?** *Complete: “Cada linha representa...”*

[preencha]

**Granularidade atual dos dados:**

[preencha]

**Unidade que quero analisar:**

[preencha]

**Preciso agregar ou transformar a granularidade antes da análise?**

[preencha]

## 3. Chaves e relacionamentos

**Chave primária ou identificador esperado:**

[preencha]

**A chave é realmente única?** *Sim / Não / Ainda não verificado*

[preencha]

**Há chave composta?**

[preencha]

**Quais chaves estrangeiras existem?**

[preencha]

### Mapeamento de tabelas

| Tabela | Granularidade | Chave | Relaciona-se com | Cardinalidade |
|------------|-------------------|-----------|----------------------|-------------------|
|            |                   |           |                      |                   |
|            |                   |           |                      |                   |
|            |                   |           |                      |                   |
|            |                   |           |                      |                   |
|            |                   |           |                      |                   |

## 4. Período e cobertura dos dados

| Item                                  | Preenchimento |
|-------------------------------------------|-------------------|
| **Menor data**                            |                   |
| **Maior data**                            |                   |
| **Granularidade temporal**                |                   |
| **Períodos ausentes?**                    |                   |
| **Cobertura suficiente para o objetivo?** |                   |

## 5. Fatos, dimensões e métricas

**Fatos** representam eventos/ocorrências na granularidade definida e podem conter várias medidas. **Dimensões** fornecem contexto para analisar esses eventos: quem, o quê, onde, quando e como.

### Fatos / eventos principais

| Fato / evento | O que representa | Granularidade |
|-------------------|----------------------|-------------------|
|                   |                      |                   |
|                   |                      |                   |
|                   |                      |                   |
|                   |                      |                   |

### Dimensões principais

| Grupo               | Colunas / atributos relevantes |
|-------------------------|------------------------------------|
| **Pessoa / Cliente**    |                                    |
| **Produto / Serviço**   |                                    |
| **Localização**         |                                    |
| **Tempo**               |                                    |
| **Processo / Operação** |                                    |

### Métricas

| Métrica | Definição | Agregação | Principal / Secundária |
|-------------|---------------|---------------|----------------------------|
|             |               |               |                            |
|             |               |               |                            |
|             |               |               |                            |
|             |               |               |                            |
|             |               |               |                            |
|             |               |               |                            |

## 6. Qualidade dos dados

### Estrutura

- [ ] Sei quantas linhas e colunas existem.
- [ ] Os tipos de dados parecem coerentes.
- [ ] Identifiquei colunas totalmente vazias ou sem utilidade.

### Nulos e duplicados

- [ ] Mapeei colunas com valores ausentes e seus percentuais.
- [ ] Entendo se o nulo significa dado faltante ou ausência real.
- [ ] Verifiquei linhas duplicadas.
- [ ] Verifiquei IDs duplicados que deveriam ser únicos.

### Valores suspeitos

**Valores impossíveis ou suspeitos encontrados:** *Ex.: idade negativa, preço \< 0, datas inesperadas, percentuais fora do domínio.*

[preencha]

## 7. Dicionário mínimo das colunas críticas

Preencha apenas as colunas que influenciam diretamente a análise. Não presuma significado apenas pelo nome.

| Coluna | Significado | Tipo | Origem | Observação / regra |
|------------|-----------------|----------|------------|------------------------|
|            |                 |          |            |                        |
|            |                 |          |            |                        |
|            |                 |          |            |                        |
|            |                 |          |            |                        |
|            |                 |          |            |                        |
|            |                 |          |            |                        |
|            |                 |          |            |                        |
|            |                 |          |            |                        |

## 8. Colunas derivadas e regras de negócio

| Campo derivado | Regra / fórmula | Por que existe? | Fonte / validação |
|--------------------|---------------------|---------------------|-----------------------|
|                    |                     |                     |                       |
|                    |                     |                     |                       |
|                    |                     |                     |                       |
|                    |                     |                     |                       |
|                    |                     |                     |                       |

## 9. Hipóteses iniciais

**Estrutura sugerida:** Fato ou métrica + dimensão + comparação.

| ID | Hipótese | Métrica / fato | Dimensão | Comparação |
|--------|--------------|--------------------|--------------|----------------|
|        |              |                    |              |                |
|        |              |                    |              |                |
|        |              |                    |              |                |
|        |              |                    |              |                |
|        |              |                    |              |                |

## 10. Comparações e referências

- [ ] Período anterior
- [ ] Mesmo período do ano anterior
- [ ] Média histórica
- [ ] Meta
- [ ] Benchmark
- [ ] Outra região / segmento / categoria

**Comparações específicas que farão sentido neste projeto:**

[preencha]

## 11. Limitações e riscos

| Limitação / risco | Impacto possível na análise | Como vou tratar / comunicar |
|-----------------------|---------------------------------|---------------------------------|
|                       |                                 |                                 |
|                       |                                 |                                 |
|                       |                                 |                                 |
|                       |                                 |                                 |
|                       |                                 |                                 |

## 12. Critério de prontidão

**Antes de avançar para o framework de análise, confirme:**

- [ ] Entendo o problema e a decisão que a análise deve apoiar.
- [ ] Sei o que uma linha representa.
- [ ] Conheço a granularidade atual e a unidade de análise desejada.
- [ ] Identifiquei as chaves e os principais relacionamentos.
- [ ] Conheço o período e a cobertura dos dados.
- [ ] Mapeei os fatos/eventos e as dimensões mais importantes.
- [ ] Defini as métricas principais e como devem ser agregadas.
- [ ] Fiz uma checagem básica de nulos, duplicados e valores suspeitos.
- [ ] Entendo o significado das colunas críticas.
- [ ] Registrei limitações relevantes.
- [ ] Tenho hipóteses iniciais ou perguntas analíticas claras.

**Próximo passo:** seguir para o seu framework de investigação analítica — problema → pergunta → hipótese → evidência → insight → decisão.

## Resumo de 1 página

| Pergunta                                      | Resposta resumida |
|---------------------------------------------------|-----------------------|
| **Qual problema estou resolvendo?**               |                       |
| **O que representa uma linha?**                   |                       |
| **Qual é a granularidade?**                       |                       |
| **Qual é a unidade de análise?**                  |                       |
| **Quais são os principais fatos/eventos?**        |                       |
| **Quais são as dimensões críticas?**              |                       |
| **Quais são as métricas principais?**             |                       |
| **Quais são as maiores limitações?**              |                       |
| **Estou pronto para iniciar a análise? Por quê?** |                       |
