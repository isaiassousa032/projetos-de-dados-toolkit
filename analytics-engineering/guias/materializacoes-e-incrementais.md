# Materializações e modelos incrementais

Escolha armazenamento pela correção, padrão de consumo e custo medido. Registre a justificativa no [template de modelo](../templates/documentacao-modelos-dbt.md).

| Materialização | Uso adequado | Custo/risco |
|---|---|---|
| View | Transformação leve e resultado consultado sobre dependências atuais | Consultas repetem processamento; não tornam ingestão mais atual |
| Table | Resultado reutilizado e reconstrução viável | Atualiza no build; reconstrução pode custar mais |
| Ephemeral | Lógica pequena incorporada aos modelos dependentes | SQL compilado cresce e não existe relação própria consultável |
| Incremental | Reconstrução total custa muito e existe regra de continuidade confiável | Exige lidar com atraso, mudanças, exclusões e recuperação |

Disponibilidade de estratégias e detalhes variam por adaptador/engine. Consulte a [configuração oficial de incrementais](https://docs.getdbt.com/docs/build/incremental-models) para a versão utilizada.

## Antes de adotar incremental

Meça volume, duração e custo de reconstrução. Confirme chave estável no grão, campo de mudança confiável e tratamento de exclusões. Uma estratégia append serve apenas quando registros são imutáveis e deduplicação está resolvida; atualizações podem exigir merge, substituição de partição ou outra estratégia suportada.

`unique_key` informa correspondência para estratégias compatíveis; não impõe unicidade e não corrige duplicações na entrada. Deduplicate com regra determinística antes de atualizar destino e teste chave nula/duplicada.

## Contrato de processamento

- **Marcador:** data de chegada/atualização ou lote; explique por que captura as mudanças necessárias.
- **Janela:** recorte reprocessado, atraso esperado e justificativa. Nenhuma janela finita captura atrasos ilimitados.
- **Atualizações:** como linhas existentes são substituídas ou reconciliadas.
- **Exclusões:** tombstones/CDC, reconstrução de partição ou limitação explícita.
- **Backfill:** como selecionar intervalo histórico sem depender apenas do último marcador.
- **Falha parcial:** quando o marcador avança e como repetir sem alterar incorretamente o estado.
- **Schema:** política para novas colunas, mudança de tipo e recálculo histórico.

## Validação com cenário controlado

| Execução | Entrada | Resultado esperado |
|---|---|---|
| Inicial | Itens A e B | Duas linhas, chave única |
| Repetição | Mesmo lote | Mesmo estado, sem duplicação |
| Correção | Valor de A alterado | Uma versão correta de A no mart corrente |
| Atraso | Item C de data antiga, recebido agora | C incorporado pela política de chegada/backfill |
| Exclusão | B excluído na origem | B tratado pela política acordada, não silenciosamente mantido |

Compare incremental com reconstrução equivalente em ambiente isolado, usando o mesmo estado de origem. Compare chaves, valores, agregados e recortes, além de contagem total. Inclua fronteiras temporais e duas mudanças com timestamp igual.

## Full refresh e histórico

Um full refresh de modelo incremental reconstrói dados e pode ter custo elevado. Confirme retenção da origem e cobertura histórica antes de usá-lo. Corrigir código sem recalcular períodos antigos pode manter divergências. Não trate snapshots históricos como caches descartáveis: a fonte corrente pode não permitir reconstruí-los.

Snapshots capturam mudanças observadas em entidades e podem apoiar SCD2; não substituem o contrato de incremental de um fato nem recuperam alterações ocorridas entre capturas quando a origem não as guarda. Defina frequência conforme necessidade de histórico.

Use [testes e qualidade](testes-e-qualidade.md) e [deploy](deploy-ci-cd-monitoramento.md) antes de mudar a estratégia de um modelo compartilhado.
