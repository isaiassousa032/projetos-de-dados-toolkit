# Boas práticas com dbt

dbt organiza transformações sobre dados disponíveis na plataforma. Use estas práticas no repositório do projeto; este toolkit contém apenas orientação e exemplos.

## Organização

- Declare sources com origem, responsável, relação física e colunas críticas. Use `source()` para referenciá-las.
- Em staging, mantenha transformação previsível por origem: nomes, tipos e convenções. Documente deduplicação e ordenação de versões.
- Use intermediate para decompor lógica complexa ou reutilizada, com grão explícito.
- Em marts, exponha modelos alinhados a processos e consumidores. Fatos e dimensões são adequados quando o consumo pede modelagem dimensional.
- Use `ref()` nas dependências dbt; nomes físicos fixos podem ocultar dependências e quebrar isolamento entre ambientes. [Referência de sources](https://docs.getdbt.com/docs/build/sources).

## SQL e configuração

Declare colunas explicitamente nos contratos de consumo; evite propagar mudanças de schema com `select *`. Organize CTEs por responsabilidade, nomeie etapas e comente a justificativa de regras não óbvias. Trate nulos conforme significado; substituir tudo por zero pode mudar métricas.

Verifique cardinalidade antes de joins. Escolha a regra de deduplicação com desempate determinístico e registre o que fazer quando não houver identificador confiável. Chaves substitutas devem representar o grão, sem esconder colisões de origem.

Fixe versões compatíveis de dbt/engine, adaptador e pacotes; confirme a sintaxe da documentação correspondente. Mantenha perfis e segredos fora do código versionado, usando o mecanismo autorizado do projeto. A [convenção do toolkit](../../compartilhado/guias/convencoes-nomenclatura-documentacao.md) usa `snake_case` nos identificadores de modelos, apesar do `kebab-case` dos documentos.

## Ciclo de desenvolvimento

1. Formule regra e resultado esperado com amostra controlada.
2. Implemente o modelo em dev e valide SQL compilado e destino.
3. Execute modelos/testes afetados, incluindo dependências e consumidores relevantes.
4. Reconcilie métricas com cálculo independente e documente diferenças.
5. Atualize descrições e revise a mudança com outra pessoa quando houver consumo compartilhado.

No dbt Core v1, comandos ilustrativos incluem `dbt build --select +fct_itens_pedido` para construir o modelo e ancestrais selecionados. Confira a seleção e inclua descendentes quando a mudança os afetar. `dbt run` executa modelos; `dbt build` integra execução e testes dos recursos selecionados segundo o DAG. [Referência do build](https://docs.getdbt.com/reference/commands/build).

## Revisão útil

Pergunte se o modelo tem propósito claro, grão estável, chave testada, tipos adequados e regras rastreáveis. Verifique comportamento de cancelamentos, estornos, atrasos e mudanças históricas. Não aceite uma consulta apenas porque compila.

Testes e documentação acompanham o código, e materialização tem justificativa. Consulte [testes](testes-e-qualidade.md), [lineage](documentacao-e-lineage.md), [incrementais](materializacoes-e-incrementais.md) e o [checklist dbt](../checklists/revisao-modelos-dbt.md).
