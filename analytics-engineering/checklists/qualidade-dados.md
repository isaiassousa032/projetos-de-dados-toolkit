# Checklist — Qualidade dos dados

Use no recorte que será entregue; retome quando fontes ou regras mudarem. Consulte [testes e qualidade](../guias/testes-e-qualidade.md).

- [ ] Unicidade e nulos são verificados no grão real dos modelos críticos.
- [ ] Domínios, tipos e significado dos valores ausentes estão confirmados.
- [ ] Chaves estrangeiras obrigatórias e referências dimensionais foram validadas.
- [ ] Cardinalidade dos joins e contagens antes/depois estão documentadas.
- [ ] Datas, vigências, timezone e fronteiras dos períodos são consistentes.
- [ ] Cancelamentos, devoluções e negativos seguem regras confirmadas.
- [ ] Regras complexas têm casos controlados de borda e resultados esperados independentes.
- [ ] Reconciliação usa a mesma população, filtros, moeda e corte da origem.
- [ ] Totais e segmentos relevantes foram comparados; tolerância tem justificativa e aprovador.
- [ ] Atualidade e cobertura foram verificadas além do status de execução.
- [ ] Incrementais foram testados com reexecução, atualização, atraso, exclusão e backfill, quando usados.
- [ ] Modelo incremental e reconstrução equivalente foram comparados em destino isolado, quando aplicável.
- [ ] Falhas críticas bloqueiam promoção/publicação afetada; avisos têm resposta e dono.
- [ ] Limitações conhecidas e riscos aceitos acompanham a entrega.

**Aceite:** nenhuma falha crítica sem resolução ou contenção acordada. Uma suíte aprovada não substitui a validação da pergunta e do significado com o consumidor.

Registro: [recorte, versão, execução, evidências, revisor e resultado].
