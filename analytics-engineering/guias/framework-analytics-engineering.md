# Framework de Analytics Engineering

Referência metodológica para construir dados analíticos confiáveis, compreensíveis e reutilizáveis. A entrega precisa conectar uma pergunta de negócio a fontes, modelos, métricas e consumo validado. Adapte a profundidade à recorrência, ao risco e à escala.

## Índice

- [Como trabalhar de forma iterativa](#como-trabalhar-de-forma-iterativa)
- [1. Definição do problema de negócio](#1-definição-do-problema-de-negócio)
- [2. Modelagem conceitual](#2-modelagem-conceitual)
- [3. Modelagem lógica](#3-modelagem-lógica)
- [4. Modelagem física](#4-modelagem-física)
- [5. Arquitetura de dados de alto nível](#5-arquitetura-de-dados-de-alto-nível)
- [6. Modelagem analítica e dimensional](#6-modelagem-analítica-e-dimensional)
- [7. Definição da granularidade](#7-definição-da-granularidade)
- [8. Implementação do Data Warehouse](#8-implementação-do-data-warehouse)
- [9. Desenvolvimento com dbt](#9-desenvolvimento-com-dbt)
- [10. Camada semântica opcional](#10-camada-semântica-opcional)
- [11. Análises com SQL](#11-análises-com-sql)
- [12. Orquestração implantação e monitoramento](#12-orquestração-implantação-e-monitoramento)
- [Marcos e encerramento](#marcos-e-encerramento)

## Como trabalhar de forma iterativa

As etapas enumeram responsabilidades, não uma ordem rígida. Investigue fontes enquanto levanta requisitos. Esboce conceito e arquitetura em paralelo. Discuta processos, medidas e grão em conjunto; **o grão precisa estar declarado antes da implementação da tabela fato**, mesmo aparecendo depois da modelagem dimensional nesta lista. Refine o desenho físico após essa decisão.

Escreva testes, documentação e consultas de validação durante o desenvolvimento. Reveja requisitos quando a origem não fornecer histórico ou cobertura suficientes. Mudanças de grão exigem revisar chaves, joins, medidas, consumidores e testes. Registre decisões e revalide os modelos dependentes.

Uma primeira entrega pode usar uma fonte já carregada, staging e um mart, com execução manual em desenvolvimento. Adicione intermediate, incremental, semântica e Airflow quando houver benefício demonstrado. dbt transforma dados disponíveis na plataforma; planeje a ingestão separadamente.

## 1. Definição do problema de negócio

**Objetivo:** acordar qual decisão será apoiada e o que caracteriza uma resposta útil.

Identifique stakeholders, responsável pela métrica, usuários e perguntas prioritárias. Delimite processo, população, período e exclusões. Diferencie entrega de objetivo: um dashboard é uma entrega; compreender onde o atendimento perde tempo é um problema. Defina métricas com fórmula, unidade, filtros, comparação, fuso e política para eventos incompletos.

Investigue acesso, sensibilidade, latência necessária, custo aceitável e critérios de aceite. Classifique requisitos obrigatórios e desejáveis, com exemplos verificáveis. Se uma fonte não permite responder à pergunta, negocie o recorte antes de implementar.

**Saída:** [requisitos](../templates/levantamento-requisitos.md), [problema](../../compartilhado/templates/descricao-problema-negocio.md) e primeiras [métricas](../templates/definicao-metricas-negocio.md).

**Pronto para avançar:** stakeholder consegue explicar decisão, população, métricas e aceite. Consulte o [guia compartilhado](../../compartilhado/guias/definicao-problema-negocio.md).

## 2. Modelagem conceitual

**Objetivo:** representar o domínio sem depender de tecnologia.

Identifique entidades, eventos, relacionamentos e regras. Em vendas, um cliente faz pedidos; pedidos possuem itens; pagamentos e devoluções são processos próprios. Registre cardinalidade, opcionalidade e exceções. Use nomes do negócio e confirme o vocabulário com os responsáveis.

**Saída:** descrição ou diagrama do domínio, glossário e regras confirmadas. Não é necessário redesenhar o sistema operacional existente.

**Pronto para avançar:** uma pessoa do negócio entende as relações e reconhece as exceções. Veja [modelagem](modelagem-de-dados.md).

## 3. Modelagem lógica

**Objetivo:** organizar atributos, chaves e relações que sustentam a implementação.

Documente o significado de cada registro, chaves naturais e compostas, nulabilidade esperada e cardinalidade. Compare o desenho com dados reais: um identificador único em uma origem pode colidir com outra. Distinga evento, entidade e versão histórica.

Normalização é útil para integridade operacional e separação de dependências; o consumo analítico pode exigir desnormalização deliberada. Registre a justificativa, sem impor terceira forma normal a todos os marts. Defina como integrar fontes e quais regras resolvem diferenças de identificação.

**Saída:** dicionário mínimo e mapa de chaves/relacionamentos.

**Pronto para avançar:** chaves e relações foram verificadas ou suas limitações estão explícitas.

## 4. Modelagem física

**Objetivo:** traduzir o desenho para o SGBD/DW escolhido.

Defina tabelas, views, tipos, precisão decimal, timestamps, schemas, constraints e permissões. Avalie índices, particionamento e clustering somente onde a plataforma os suporta e consultas justificam. Confirme quais constraints são efetivamente impostas pelo DW; constraints declarativas não substituem testes de unicidade e integridade.

Esboce aqui e refine após declarar grão e medidas. Preserve precisão monetária, significado de nulos e convenção de fuso. Estime custo com consultas representativas antes de otimizar.

**Saída:** especificação implementável e decisão de armazenamento/materialização.

**Pronto para avançar:** desenho preserva o significado lógico e atende aos padrões de consulta. Use o [registro arquitetural](../templates/decisoes-arquiteturais.md).

## 5. Arquitetura de dados de alto nível

**Objetivo:** explicitar o percurso dos dados e a responsabilidade de cada componente.

Descreva fontes → ingestão → armazenamento bruto → transformação → consumo. Escolha carga completa, incremental ou CDC conforme volume, mudanças e disponibilidade. Inclua histórico, exclusões, mudanças de schema, recuperação e controle de acesso. Defina responsável por cada fronteira.

ELT permite transformar após carregar; certas regras podem ocorrer antes por segurança ou formato. Não materialize todas as camadas por hábito. Documente limitações, frequência, dependências e onde cada regra é aplicada.

**Saída:** desenho de alto nível e decisões justificadas. Consulte [arquitetura e camadas](arquitetura-e-camadas.md).

**Pronto para avançar:** sabe-se de onde cada dado vem, como chega e quem responde por falhas.

## 6. Modelagem analítica e dimensional

**Objetivo:** organizar processos de negócio para análise consistente.

Selecione um processo prioritário e, em conjunto com a etapa 7, declare seu grão. Identifique fatos transacionais, snapshots periódicos ou acumulativos, dimensões e medidas. Defina dimensões conformadas quando processos compartilham conceitos. Classifique medidas aditivas, semiaditivas e não aditivas.

Decida histórico por atributo: tipo 1 para estado corrente; tipo 2 quando o contexto à época do evento importa. Uma dimensão SCD2 precisa de chave da versão, intervalos de vigência sem sobreposição e associação temporal correta do fato. Capturas futuras não recuperam histórico inexistente.

**Saída:** [documentação dimensional](../templates/modelagem-dimensional.md), medidas, regras históricas e consumidores.

**Pronto para avançar:** perguntas prioritárias podem ser respondidas sem mistura indevida de processos. Consulte o [exemplo ilustrativo](../exemplos/modelagem-vendas.md).

## 7. Definição da granularidade

**Objetivo:** garantir que chaves, joins e medidas expressem a mesma unidade.

Escreva: “Cada linha representa…”. Inclua origem, evento, item, intervalo ou posição temporal quando necessário. “Um item identificado por `item_id` dentro de um pedido” é mais preciso que “uma venda”. `pedido_id + produto_id` não identifica uma linha se o mesmo produto puder repetir no pedido.

Declare também o grão de cada dimensão: uma entidade atual ou uma versão histórica. Teste unicidade no grão real e cardinalidades dos joins. Atributos dimensionais devem depender da chave/versão definida; medidas devem pertencer à ocorrência representada.

Para combinar dois fatos, agregue primeiro ao grão comum ou defina uma associação validada. Não some o valor do pedido depois de repeti-lo em todos os itens. Trate saldos ao longo do tempo e recalcule taxas a partir de componentes compatíveis.

**Saída:** declaração de grão e verificações por modelo.

**Pronto para avançar:** não há ambiguidade sobre uma linha e nenhuma medida muda por multiplicação inesperada em joins. Use a [revisão de modelagem](../checklists/revisao-modelagem.md).

## 8. Implementação do Data Warehouse

**Objetivo:** disponibilizar uma base lógica segura, rastreável e recuperável.

No repositório do projeto, prepare schemas de bruto e transformação/consumo, ambientes isolados e acessos mínimos. Registre metadados de origem, lote e momento de carga. Escolha armazenamento conforme volume, retenção e consultas, incluindo política de recuperação.

Valide carga inicial e continuidade. Reexecuções devem produzir o estado esperado sem duplicação; só avance marcadores após carga bem-sucedida. Reconcilie contagens e valores no mesmo recorte da fonte. Diferencie data do evento, data de chegada e estado completo do lote.

**Saída:** entradas acessíveis e procedimento de carga, backfill e recuperação documentado.

**Pronto para avançar:** dados mínimos necessários estão disponíveis e reconciliados. Esta biblioteca não cria infraestrutura nem armazena credenciais.

## 9. Desenvolvimento com dbt

**Objetivo:** tornar transformações reproduzíveis, testáveis e legíveis.

Declare sources; padronize nomes e tipos em staging; use intermediate para integrações reutilizadas ou complexas; entregue fatos, dimensões ou modelos de consumo em marts. Use `source()` para entradas e `ref()` para dependências. Uma camada intermediate é opcional.

Escolha materializações pela necessidade. Comece simples e adote incremental após medir benefício e validar atrasos, atualizações, exclusões e recuperação. Definir `unique_key` não comprova unicidade. Fixe versões compatíveis de engine, adaptador e pacotes no projeto.

Documente propósito, grão, colunas, regras e limitações. Combine testes de dados, lógica e reconciliação. Faça revisão técnica de filtros, nulos, joins e consumidores afetados.

**Saída:** modelos, testes e documentação no projeto; [ficha do modelo](../templates/documentacao-modelos-dbt.md).

**Pronto para avançar:** modelo responde à pergunta e reconcilia com referência independente. Consulte [dbt](boas-praticas-dbt.md), [testes](testes-e-qualidade.md) e [incrementais](materializacoes-e-incrementais.md).

## 10. Camada semântica opcional

**Objetivo:** compartilhar definições de métricas entre consumidores quando a necessidade justificar.

Defina medidas, dimensões, entidades, tempo, filtros e caminhos de relacionamento. Valide taxas e contagens distintas para todos os cortes permitidos. Avalie o dbt Semantic Layer quando engine, versão, plataforma e interfaces de consumo forem compatíveis. Não é requisito para começar: marts documentados podem bastar.

**Saída:** catálogo de métricas e, se adotada, configuração semântica no projeto.

**Pronto para avançar:** resultados equivalem a consultas de referência e definições têm responsável e política de mudança. Consulte [camada semântica](camada-semantica.md).

## 11. Análises com SQL

**Objetivo:** demonstrar utilidade e validar métricas com perguntas reais.

Consulte marts, verifique grão, população e completude; use staging/raw quando investigar diferenças. Organize consultas em CTEs, explicite filtros e evite joins que multipliquem medidas. Compare períodos equivalentes, trate denominador zero e distinga data do evento de data de processamento.

Reconcilie com fonte ou cálculo independente usando os mesmos cortes. Registre diferenças e limitações antes de comunicar resultados. SQL correto sintaticamente não garante definição correta do negócio.

**Saída:** consultas de validação, resultados e aceite do consumidor. Veja [consultas ilustrativas](../exemplos/consultas-analiticas.md).

**Pronto para avançar:** stakeholder reconhece a métrica e consegue usar a entrega. A investigação pode seguir o [Lite](../../analise-de-dados/lite/README.md) ou o [Completo](../../analise-de-dados/completo/README.md).

## 12. Orquestração implantação e monitoramento

**Objetivo:** operar uma entrega validada com controles proporcionais ao impacto.

Prepare CI com validação em ambiente isolado, testes e revisão. Planeje deploy, mudanças incompatíveis, backfill e recuperação. Reverter código não necessariamente reverte dados. Registre versão implantada, execute verificações de consumo e obtenha aceite.

Após o pipeline funcional, escolha a forma de execução recorrente. Airflow é útil quando dependências entre sistemas, retries, backfills e operação justificam sua manutenção; um agendamento simples pode ser suficiente. Defina intervalos de processamento, idempotência, falhas e responsáveis.

Monitore execução, freshness, cobertura, qualidade, duração e custo. `dbt build` organiza os recursos selecionados segundo o DAG; freshness das sources é uma verificação distinta. Um job bem-sucedido pode ter dados incompletos. Alertas devem informar impacto e ação esperada.

**Saída:** plano de deploy, runbook, monitoramento e [checklist de entrega](../checklists/deploy-entrega-final.md).

**Pronto para operar:** primeiro ciclo validado, consumidores informados e recuperação compreendida. Consulte [deploy e operação](deploy-ci-cd-monitoramento.md).

## Marcos e encerramento

| Marco | Evidência mínima |
|---|---|
| Problema acordado | Pergunta, métrica, população e aceite registrados |
| Modelo pronto | Grão, chaves, medidas e histórico consistentes com fontes |
| Primeira entrega validada | Modelo testado, documentado e reconciliado com pergunta respondida |
| Entrega operável | Versão conhecida, consumo validado e resposta a falhas definida |

Encerre o escopo quando os critérios de aceite forem atendidos e os riscos remanescentes tiverem responsáveis. Evoluções entram em novo recorte, com prioridade pelo valor de negócio. Evite exigir todas as ferramentas para comprovar uma entrega pequena.

Base de apoio: [guia geral fornecido](../../recursos/referencias/materiais/guia-geral-analytics-engineering.pdf). As referências técnicas e as limitações dos materiais estão no [índice de estudos](../../recursos/referencias/README.md). Este framework é uma síntese adaptada ao toolkit.
