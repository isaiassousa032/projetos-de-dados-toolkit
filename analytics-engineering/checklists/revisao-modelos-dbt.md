# Checklist — Revisão de modelos dbt

Use em mudanças de modelos e propriedades. Consulte [boas práticas](../guias/boas-praticas-dbt.md) e a [ficha do modelo](../templates/documentacao-modelos-dbt.md).

- [ ] Propósito, camada, consumidor, grão e chave são explícitos.
- [ ] Sources e dependências usam `source()` e `ref()` quando correspondem a recursos dbt.
- [ ] Filtros, nulos e deduplicação refletem regras de negócio, com desempate determinístico.
- [ ] Joins e agregações não multiplicam medidas nem misturam grãos.
- [ ] Colunas de consumo são explícitas e têm nomes, tipos e unidades consistentes.
- [ ] Materialização tem justificativa de uso/custo; incremental não foi adotado por hábito.
- [ ] Incremental define chave, marcador, atraso, updates, deletes, schema e recuperação, se aplicável.
- [ ] Modelos e colunas críticas possuem descrições e testes pertinentes.
- [ ] Validação inclui dados e casos independentes da lógica implementada.
- [ ] Seleção executada cobre ancestrais e consumidores afetados pela mudança.
- [ ] Freshness foi verificada separadamente quando necessária ao consumo.
- [ ] Engine, adaptador e pacotes têm versões compatíveis identificadas.
- [ ] Execução ocorreu no destino esperado, sem credenciais no código ou logs.
- [ ] Mudança de contrato/histórico foi comunicada e tem transição documentada.
- [ ] Documentação e lineage representam o comportamento entregue.

**Pronto para revisão final:** evidências de execução e reconciliação acompanham a mudança, e limitações estão claras.

Registro: [modelo, versão, revisor, recorte e resultado].
