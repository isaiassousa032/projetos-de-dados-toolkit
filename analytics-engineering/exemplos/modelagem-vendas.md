# Exemplo ilustrativo — Modelagem de vendas

Caso fictício para discutir grão, medidas e histórico. Não é um projeto completo nem representa resultados reais.

## Problema e fontes

Pergunta: qual é a receita dos pedidos elegíveis por categoria em janeiro de 2026? O exemplo define receita como valor dos itens, descontados os descontos do item, excluindo pedidos cancelados. Impostos, frete, pagamentos e devoluções estão fora deste recorte; uma métrica real deve decidir explicitamente esses componentes.

Fontes conceituais: pedidos com cliente, data e status; itens com identificador próprio, pedido, produto, quantidade, preço e desconto; produtos com categoria. Um pedido pode conter o mesmo produto em mais de um item.

## Desenho

| Modelo | Grão | Chave | Conteúdo |
|---|---|---|---|
| `fct_itens_pedido` | Um item identificado dentro de um pedido de uma origem | `origem + pedido_id + item_id` | Quantidade e receita elegível do item |
| `dim_produto` | Um produto atual da origem | `origem + produto_id` ou substituta correspondente | Nome e categoria corrente |
| `dim_cliente` | Um cliente atual da origem | `origem + cliente_id` | Segmento corrente |
| `dim_data` | Um dia do calendário | `data` | Mês, ano e calendário de negócio |

O exemplo usa tipo 1 e classifica pela categoria corrente. Para categoria vigente na venda, altere `dim_produto` para tipo 2, associe pela vigência do evento e teste intervalos. Não afirme que o cadastro atual permite reconstruir todas as categorias passadas.

## Amostra controlada

| Pedido | Item | Produto | Quantidade | Preço unitário | Desconto do item | Receita do item | Status |
|---|---|---|---:|---:|---:|---:|---|
| 10 | 1 | A | 2 | 50 | 10 | 90 | concluído |
| 10 | 2 | B | 1 | 80 | 0 | 80 | concluído |
| 11 | 1 | A | 1 | 50 | 0 | 50 | concluído |
| 12 | 1 | B | 1 | 80 | 0 | 80 | cancelado |

Receita elegível: **220**. Pedidos elegíveis: **2**. Ticket médio: **110**. Se A for categoria X e B for Y, receitas por categoria são 140 e 80. Somar totais de pedido repetidos em itens produziria erro; média dos três itens elegíveis seria aproximadamente 73,33, que não é ticket por pedido.

## Contrato de medidas

`receita_item = quantidade × preco_unitario − desconto_item`. Desconto é valor total do item neste exemplo, não percentual nem desconto por unidade. A receita é aditiva entre itens elegíveis na mesma moeda. Quantidade tem unidade de item/produto e pode não ser comparável entre produtos com unidades distintas.

Pagamento é outro processo. Não faça join de itens e pagamentos por pedido sem avaliar multiplicação. Para comparar receita pedida e recebida, agregue cada processo ao grão comum ou documente alocação.

## Validação esperada

- Chave do item única/não nula; pedido obrigatório e existente.
- Produtos/datas encontrados nas dimensões, com política explícita para desconhecidos.
- Join de produto preserva linhas e receita, com uma correspondência por item.
- Receita 220, contagem de pedidos 2 e ticket 110 com os filtros acordados.
- Cancelado excluído; limite histórico do tipo 1 comunicado.

Veja [consultas SQL](consultas-analiticas.md), [trechos dbt](trechos-dbt.md) e o [template dimensional](../templates/modelagem-dimensional.md).
