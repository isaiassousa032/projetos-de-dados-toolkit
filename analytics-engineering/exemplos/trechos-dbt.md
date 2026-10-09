# Exemplos ilustrativos — Sources, staging e testes dbt

Trechos didáticos que devem ser adaptados no projeto. Não constituem projeto executável. Sintaxe de `data_tests` com `arguments` segue a documentação dbt v1.10.5+; confirme engine, adaptador e versão. As tabelas de origem já precisam existir.

## Source e staging

Declaração ilustrativa de propriedades:

```yaml
version: 2
sources:
  - name: comercial
    schema: raw_comercial
    tables:
      - name: itens_pedido
        description: Itens capturados do sistema comercial, antes de filtros de consumo.
        columns:
          - name: item_id
            data_tests:
              - not_null
```

Staging ilustrativo; `item_id` só será chave se sua unicidade estiver definida no grão:

```sql
select
    origem,
    pedido_id,
    item_id,
    produto_id,
    quantidade,
    cast(preco_unitario as decimal(18, 2)) as preco_unitario,
    cast(desconto_item as decimal(18, 2)) as desconto_item
from {{ source('comercial', 'itens_pedido') }}
```

Não substitua nulos por zero sem confirmar significado. Tipos e sintaxe devem ser compatíveis com o DW. Sources documentam entradas; não carregam dados.

## Testes de propriedade

Supondo que `item_pedido_sk` represente a combinação validada de origem, pedido e item, e que `produto_sk` referencie uma dimensão com chave única:

```yaml
version: 2
models:
  - name: fct_itens_pedido
    description: Um item identificado de um pedido por origem.
    columns:
      - name: item_pedido_sk
        data_tests:
          - unique
          - not_null
      - name: produto_sk
        data_tests:
          - not_null
          - relationships:
              arguments:
                to: ref('dim_produto')
                field: produto_sk
```

Uma chave substituta não demonstra que os atributos que a geraram eram suficientes. Valide a combinação natural e o grão também.

## Teste singular

Consulta ilustrativa para retornar itens com valores obrigatórios ausentes ou quantidade inválida. A regra assume vendas de quantidade positiva; estornos precisariam de outro contrato.

```sql
select origem, pedido_id, item_id, quantidade, preco_unitario
from {{ ref('stg_comercial__itens_pedido') }}
where quantidade is null
   or quantidade <= 0
   or preco_unitario is null
```

No projeto, salve em `tests/` e execute com seleção apropriada. Zero linhas significa aprovação da condição, não validade de toda a métrica.

## O que falta para um projeto real

Perfis, fontes carregadas, modelos relacionados, chaves e filtros de elegibilidade, configurações, testes completos e reconciliação. Adapte tudo no repositório do projeto; não execute estes trechos como infraestrutura.

Referências: [sources](https://docs.getdbt.com/docs/build/sources) e [data tests](https://docs.getdbt.com/docs/build/data-tests). Consulte [boas práticas](../guias/boas-praticas-dbt.md).
