# Documentação e lineage

Documentação útil permite entender significado, avaliar confiança e operar mudanças. Use a [ficha de modelo](../templates/documentacao-modelos-dbt.md) e atualize-a junto do código.

## O que registrar

| Objeto | Conteúdo mínimo |
|---|---|
| Source | Origem, responsável, frequência, cobertura, histórico e limitações |
| Modelo | Propósito, grão, chave, dependências, regras e materialização |
| Coluna crítica | Significado, unidade, tipo, nulos e origem/derivação |
| Métrica | População, fórmula, tempo, filtros, agregação e dono |
| Consumidor | Modelo utilizado, responsável e impacto de mudança |
| Operação | Execução, resposta a falha, backfill e recuperação |

Descreva por que uma regra existe. “Soma a coluna valor” não explica se ela inclui impostos, cancelamentos ou devoluções. Evite copiar toda a SQL para o dicionário: registre semântica e decisões e referencie o código.

## Lineage prático

No dbt, `source()` e `ref()` registram dependências no grafo. Complete essa visão com ingestão, fontes externas, BI e exports. Um grafo automático pode não capturar processamento fora do dbt ou consultas que usam nomes físicos diretamente. [Referência de sources e DAG](https://docs.getdbt.com/docs/build/sources).

Para uma mudança, trace origem → modelos afetados → métricas → consumidores. Verifique impacto em grão, schema, valores e histórico. Para uma falha, siga o caminho inverso, comparando o primeiro ponto onde dados deixam de atender à regra.

## Documentação próxima ao desenvolvimento

1. Escreva descrições e propriedades ao criar modelo e colunas críticas.
2. Registre decisão importante em [ADR](../templates/decisoes-arquiteturais.md), incluindo alternativas e consequência.
3. Identifique consumidores e responsáveis antes de alterar contrato.
4. Gere/atualize o catálogo compatível com a engine e ferramenta adotadas.
5. Revise exemplos, data de revisão e procedimento operacional na mesma mudança.

No Core v1, `dbt docs generate` gera artefatos para documentação; confira destino, disponibilidade de metadados e permissões antes de compartilhar. Catálogos podem expor nomes de objetos e lógica de negócio. Nunca inclua segredos, amostras pessoais ou credenciais em descrições e logs.

## Runbook mínimo

Registre sintoma, consulta de diagnóstico, responsável, contenção, comando/procedimento de reprocessamento no projeto, custo previsto e verificação posterior. Especifique quando escalar para a equipe da origem. A recuperação deve produzir dados coerentes, não apenas uma execução verde.

Veja [convenções compartilhadas](../../compartilhado/guias/convencoes-nomenclatura-documentacao.md) e [documentação em DataOps](../../recursos/dataops/documentacao.md).
