# Checklist — Revisão de modelagem

Revise antes de implementar e sempre que mudar grão ou histórico. Use o [template dimensional](../templates/modelagem-dimensional.md).

- [ ] Entidades, eventos, regras e cardinalidades foram reconhecidos pelo negócio.
- [ ] Cada fato declara exatamente o que uma linha representa.
- [ ] Chaves incluem todos os atributos necessários, inclusive origem ou versão quando pertinente.
- [ ] A combinação de chaves foi verificada contra dados reais.
- [ ] Cada dimensão declara entidade corrente ou versão histórica.
- [ ] Medidas pertencem ao grão e suas agregações permitidas estão registradas.
- [ ] Totais de outro grão não são repetidos e somados indevidamente.
- [ ] Taxas/médias podem ser recalculadas com componentes e pesos corretos.
- [ ] Dimensões conformadas usam significado e identificação compatíveis entre processos.
- [ ] SCD2 define vigência, associação do fato e teste de não sobreposição, quando adotada.
- [ ] Unknowns, entidades anônimas e dimensões tardias têm tratamento explícito.
- [ ] Muitos para muitos e joins entre fatos têm ponte, alocação ou grão comum validado.
- [ ] Joins preservam cardinalidade e valores esperados, incluindo casos sem correspondência.
- [ ] Tipos, precisão, constraints e otimizações correspondem à plataforma escolhida.
- [ ] Consultas prioritárias são possíveis, sem atribuir histórico que não existe.

**Aprovar o desenho:** não existem ambiguidades de grão que alterem métricas. Documente riscos aceitos e responsáveis.

Registro: [versão, data, revisor, evidências e decisões].
