# Exemplos ilustrativos — Consultas analíticas e validação

As consultas usam o [caso fictício de vendas](modelagem-vendas.md). Assuma origem única `loja-a`, um fato com `receita_item`, `status_pedido`, `data_pedido` e chaves substitutas; datas já estão no fuso de negócio. Adapte relações e dialeto. Não há conexão ou banco produtivo neste toolkit.

## Receita e ticket por período

```sql
select
    sum(receita_item) as receita,
    count(distinct pedido_id) as pedidos,
    sum(receita_item) / nullif(count(distinct pedido_id), 0) as ticket_medio
from fct_itens_pedido
where origem = 'loja-a'
  and status_pedido = 'concluido'
  and data_pedido >= date '2026-01-01'
  and data_pedido < date '2026-02-01';
```

Esperado na amostra: 220, 2 e 110. Em múltiplas origens, conte pedidos por chave composta validada ou substituta, evitando colisão de `pedido_id`. Confirme divisão decimal no dialeto e comportamento de um período sem registros.

## Receita por categoria

```sql
select
    p.categoria,
    sum(f.receita_item) as receita
from fct_itens_pedido f
left join dim_produto p on f.produto_sk = p.produto_sk
where f.origem = 'loja-a'
  and f.status_pedido = 'concluido'
  and f.data_pedido >= date '2026-01-01'
  and f.data_pedido < date '2026-02-01'
group by p.categoria;
```

Esperado: X = 140 e Y = 80. O `left join` preserva itens sem dimensão para diagnóstico, mas não impede duplicação caso `produto_sk` se repita. Confirme chave única da dimensão e trate categoria desconhecida conforme contrato.

## Grão e correspondência

```sql
select origem, pedido_id, item_id, count(*) as ocorrencias
from fct_itens_pedido
group by origem, pedido_id, item_id
having count(*) > 1;
```

Esperado: zero linhas. Verifique nulos separadamente. Para detectar produto ausente ou duplicado na dimensão:

```sql
select f.item_pedido_sk, count(p.produto_sk) as correspondencias
from fct_itens_pedido f
left join dim_produto p on f.produto_sk = p.produto_sk
group by f.item_pedido_sk
having count(p.produto_sk) <> 1;
```

Esperado: zero linhas após assegurar a chave do fato única. SCD2 exige chave de versão ou condição de vigência; juntar somente pela chave natural pode multiplicar fatos.

## Reconciliação

Calcule contagem de itens, pedidos distintos e receita na origem com os mesmos filtros e compare ao mart por dia/categoria. Explique diferenças por corte, estados, arredondamento ou dado ausente. Totais iguais não dispensam verificar os segmentos; preserve consultas e resultados como evidência no projeto.

Consulte [testes](../guias/testes-e-qualidade.md) e o [template de métrica](../templates/definicao-metricas-negocio.md).
