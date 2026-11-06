# Checklist — Pipeline de dados

Use antes de considerar a ingestão e o pipeline prontos. Registre evidência ou justificativa de não aplicabilidade. Referências: [ingestão idempotente](../guias/ingestao-idempotente.md), [arquitetura em camadas](../guias/arquitetura-medalhao.md) e [orquestração](../guias/orquestracao-airflow.md).

## Ingestão

- [ ] Rodar a mesma data duas vezes não duplica nem altera a contagem.
- [ ] Um backfill de intervalo gera exatamente as partições esperadas.
- [ ] Fonte vazia, parcial ou com erro interrompe a execução e não grava arquivo.
- [ ] A escrita é atômica (arquivo temporário e renomeação).
- [ ] Toda linha tem origem e momento da ingestão.
- [ ] Data de referência, de atualização e de ingestão estão distinguidas, e há janela de reprocesso para atualizações tardias.
- [ ] Erros temporários têm nova tentativa com espera; erros permanentes falham de imediato.

## Camadas

- [ ] A Bronze não sofre renomeação, filtro nem regra após a gravação.
- [ ] A RAW é recriada a partir da Bronze sem passo manual e a contagem confere.
- [ ] Se a fonte não guarda histórico, existe cópia da Bronze fora da máquina.
- [ ] Silver e Gold passaram pelos checklists de [revisão dos modelos dbt](../../analytics-engineering/checklists/revisao-modelos-dbt.md) e de [qualidade dos dados](../../analytics-engineering/checklists/qualidade-dados.md).

## Orquestração (se houver)

- [ ] O pipeline funcionava à mão antes de ser agendado.
- [ ] A DAG usa a data do intervalo, nunca o relógio.
- [ ] `catchup` está explícito e `max_active_runs` é compatível com o banco.
- [ ] Reexecutar uma data não duplica nada.
- [ ] Uma falha gera um sinal que alguém vê (veja [monitoramento](../../recursos/dataops/ci-cd-e-monitoramento.md#monitoramento)).

## Segurança e reprodução

- [ ] Nenhum segredo em código, logs, commits ou histórico do Git.
- [ ] Um clone limpo reproduz o pipeline seguindo só o README.
- [ ] As versões das dependências estão fixadas.

**Pronto para publicar:** todos os itens aplicáveis marcados, com evidência. Se algum falhar, corrija antes de automatizar ou divulgar.

Registro: [projeto, data, responsável, evidências e exceções aceitas].

[Voltar à Engenharia de Dados](../README.md).
