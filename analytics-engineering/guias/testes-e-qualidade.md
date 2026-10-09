# Testes e qualidade de dados

Comece pelos riscos que podem mudar uma decisão. O [guia compartilhado](../../compartilhado/guias/qualidade-de-dados.md) define dimensões de qualidade; este guia detalha sua aplicação a modelos e dbt.

## Camadas de evidência

| Verificação | Detecta | Exemplo |
|---|---|---|
| Teste unitário | Erro de lógica com entradas controladas | Item cancelado não entra na receita |
| Teste de dados | Violação no estado das relações | Chave do item repetida ou nula |
| Reconciliação | Divergência entre origem e transformação | Receita por dia/canal com mesmos filtros |
| Integração/consumo | Quebra entre modelos e consumidores | Consulta de BI com colunas esperadas |
| Operação | Dados atrasados, incompletos ou fora de padrão | Lote incompleto apesar de execução concluída |

Uma suíte aprovada comprova as condições testadas; não garante todas as interpretações possíveis.

## Plano mínimo por modelo crítico

1. Identifique grão e chave. Teste unicidade e obrigatoriedade separadamente.
2. Defina domínio dos atributos e semântica dos nulos.
3. Teste referências dimensionais e cardinalidade esperada após joins.
4. Teste regras críticas: datas de término, população elegível, sinal de estornos e duplicação de medidas.
5. Reconcilie contagens e somas por período e segmento relevante.
6. Defina freshness e cobertura com base no consumo, incluindo responsável e resposta à falha.

Os testes genéricos nativos incluem `unique`, `not_null`, `accepted_values` e `relationships`. Testes singulares retornam linhas que violam uma regra; nenhuma linha retornada significa aprovação dessa regra. Exemplos e sintaxe estão na [documentação de data tests](https://docs.getdbt.com/docs/build/data-tests) e nos [trechos didáticos](../exemplos/trechos-dbt.md).

Para chaves compostas, verifique a combinação completa. `relationships` não substitui `not_null` quando a chave estrangeira é obrigatória. Testes de domínio que ignoram nulos também precisam de obrigatoriedade quando pertinente.

## Reconciliação e tolerância

Compare a mesma população, período, timezone, moeda, status e corte de processamento. Especifique diferença absoluta e relativa e registre o responsável por aprovar tolerância. Não use um percentual padrão sem avaliar impacto; contagens de chave podem exigir diferença zero, enquanto conversão monetária exige regra explícita de arredondamento.

Se os totais forem iguais, confirme também cortes relevantes: erros podem se compensar entre categorias. Consulte as [consultas de validação](../exemplos/consultas-analiticas.md).

## Casos de borda

- Reexecutar um lote sem duplicar ou perder registros.
- Atualização tardia, exclusão na origem e backfill sobre períodos já carregados.
- Grão com múltiplas fontes e IDs iguais.
- Denominador zero, ausência de eventos e timestamps na fronteira do período.
- SCD2 com versões adjacentes, corrente, desconhecida e sem sobreposição.

## Como reagir à falha

Registre execução, período afetado, condição violada e consumidor em risco. Bloqueie promoção/publicação de resultados críticos até decidir correção ou contenção; avisos também precisam de dono e prazo. Investigue origem e SQL compilado, corrija a causa, reexecute o recorte afetado e reconcilie novamente. Evite apagar registros apenas para deixar testes verdes.

Freshness é distinta de `dbt build`; execute a verificação correspondente à versão adotada. Para Core v1, consulte [source freshness](https://docs.getdbt.com/reference/commands/source). Use o [checklist de qualidade](../checklists/qualidade-dados.md).
