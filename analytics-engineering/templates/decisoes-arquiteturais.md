# ADR [número] — [decisão]

Use para escolhas com alternativas e consequências relevantes. Uma decisão simples pode ser registrada na ficha do modelo. Consulte [arquitetura e camadas](../guias/arquitetura-e-camadas.md).

- Estado: [proposta/aceita/substituída/rejeitada].
- Data e responsáveis: [identificação].
- Escopo e requisitos atendidos: [problema e restrições].
- Decisão substituída, se houver: [referência].

## Contexto

[Descreva a necessidade, estado atual, fontes, volume, histórico, consumidores e restrições. Separe fatos confirmados de estimativas.]

## Alternativas

| Alternativa | Benefícios | Custos/riscos | Requisitos atendidos | Evidências |
|---|---|---|---|---|
| [opção A] | [benefício] | [limitação] | [requisito] | [medição/documentação] |
| [opção B] | [benefício] | [limitação] | [requisito] | [medição/documentação] |

## Decisão e justificativa

[Escolha e explique por que é adequada a este escopo. Exemplos: table antes de incremental; agendamento simples antes de Airflow; tipo 1 em atributo sem requisito histórico.]

## Consequências e implantação

- Benefícios esperados e como medir: [critério].
- Custos operacionais e limitações aceitas: [impacto e responsável].
- Segurança e acesso: [papéis, sem segredos].
- Modelos/consumidores afetados: [lista e transição].
- Migração/backfill: [procedimento e validação].
- Recuperação: [como desfazer código e restaurar/reprocessar dados].

## Revisão

- Condições para reavaliar: [volume, frequência, consumidores, risco].
- Evidência de aceite: [data, responsável e resultado].
- Próxima decisão, se substituída: [referência].
