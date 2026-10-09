# Levantamento de requisitos — [projeto]

Copie para o projeto e registre respostas verificáveis. Marque o que não se aplica com justificativa. Use o [guia compartilhado](../../compartilhado/guias/levantamento-requisitos.md) para conduzir a conversa.

## Contexto e responsabilidades

- Data e versão: [data/revisão].
- Problema e decisão: [descrição ou referência ao registro do problema].
- Stakeholder e aprovador: [pessoa/papel].
- Responsável técnico e dono dos dados: [pessoa/papel].
- Consumidores: [SQL, BI, aplicação; responsáveis].
- Processo prioritário: [processo de negócio].
- Escopo incluído/excluído: [população, períodos, processos e limites].

## Perguntas e entregas

| ID | Pergunta/necessidade | Entrega esperada | Prioridade | Critério de aceite | Quem valida |
|---|---|---|---|---|---|
| R01 | [pergunta] | [modelo/consulta/relatório] | [obrigatória/desejável] | [exemplo verificável] | [papel] |

## Fontes e restrições

| Fonte | Autoridade para | Grão/chave | Cobertura/histórico | Atualização | Acesso/responsável | Limitação |
|---|---|---|---|---|---|---|
| [origem] | [conceito] | [unidade/ID] | [período] | [frequência/corte] | [papel] | [lacuna] |

- Eventos atrasados, atualizações e exclusões: [comportamento e captura].
- Sensibilidade e uso permitido: [classificação e controles, sem dados pessoais ou segredos].
- Retenção necessária: [prazo e justificativa].

## Métricas e operação

- Métricas prioritárias: [nome e referência à ficha de definição].
- Fuso, calendário, moeda e unidades: [convenções].
- Horário de disponibilidade e latência: [necessidade do consumidor].
- Frequência de processamento: [frequência justificada].
- Volume/custo/desempenho aceitáveis: [medida e limite acordados].
- Falha crítica e responsável por resposta: [impacto e papel].
- Dependências externas: [equipes/sistemas e acordo].

## Validação e aceite

| Critério | Método | Resultado esperado/tolerância | Evidência | Responsável |
|---|---|---|---|---|
| [regra] | [teste/reconciliação/uso real] | [limite justificado] | [local no projeto] | [papel] |

- Questões em aberto: [questão, impacto, responsável e data de resolução].
- Riscos aceitos: [risco, mitigação e aprovador].
- Registro de aceite: [data, versão, aprovador e observações].

Próximo passo: [modelagem dimensional](modelagem-dimensional.md) e [definição das métricas](definicao-metricas-negocio.md).
