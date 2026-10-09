# Exemplo ilustrativo — Receita por canal

Caso fictício e pequeno para demonstrar o método Completo. Não representa projeto concluído, resultado real ou evidência causal.

## Entender

A equipe quer decidir onde investigar uma redução de receita. A base hipotética contém itens de pedidos, com pedido, canal, data, status e receita do item. Grão: item identificado dentro de um pedido. A análise será por canal em dois meses completos, na mesma moeda, excluindo cancelados em ambos.

Diagnóstico: chaves únicas, ausência de nulos em canal/valor, cobertura equivalente e totais reconciliados são condições assumidas do exemplo, não verificações executadas sobre uma base real. Em um projeto, registre a evidência dessas condições no [diagnóstico inicial](../templates/template-diagnostico-inicial.docx).

## Pergunta e hipótese

Pergunta: quais canais contribuíram para a redução de receita entre janeiro e fevereiro de 2026?

H01: a redução está concentrada no canal online. Prioridade alta, pois permite direcionar a próxima investigação. Subperguntas: quanto mudou no total; quanto cada canal contribuiu; a cobertura e os filtros são comparáveis?

## Evidências fictícias

| Canal | Janeiro | Fevereiro | Variação absoluta |
|---|---:|---:|---:|
| Online | 1.000 | 700 | -300 |
| Loja | 1.000 | 1.000 | 0 |
| Total | 2.000 | 1.700 | -300 |

Variação total: -15%. Online concentra 100% da redução absoluta neste cenário. H01 é consistente com os dados ilustrativos.

## Interpretar e comunicar

Achado: receita online diminuiu 300. Insight: neste recorte, a queda total está concentrada em um canal, justificando investigar esse canal primeiro. Recomendação: decompor online por volume de pedidos, ticket e categoria antes de aplicar ações a todos os canais.

Limitações: dois meses não demonstram sazonalidade, cobertura assumida precisa ser comprovada, e concentração não explica causa. Nenhum efeito de preço, mídia ou experiência do cliente foi demonstrado.

## Encerrar o recorte

A pergunta sobre contribuição por canal está respondida no cenário fictício. A investigação causal e a decomposição do online são próximos recortes. Use o [template de resumo executivo](../templates/template-resumo-executivo.docx) para apresentar decisão, evidência e limites em um projeto real.
