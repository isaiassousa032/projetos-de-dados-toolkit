# Métrica de negócio — [nome]

Use uma ficha por métrica prioritária. Não depende de camada semântica ou fornecedor. Consulte o [guia de problema](../../compartilhado/guias/definicao-problema-negocio.md).

## Significado e uso

- Nome e identificador: [nome de negócio e identificador técnico].
- Pergunta/decisão apoiada: [uso].
- Responsável pelo significado e aprovador: [papéis].
- Unidade, moeda e precisão: [convenção].
- Versão e data da definição: [registro].

## População e cálculo

- Fonte/modelo de autoridade: [relação e grão].
- População elegível: [quem/o que entra].
- Filtros e exclusões: [status, testes, cancelamentos etc.].
- Fórmula: [expressão inequívoca].
- Numerador e denominador, quando aplicável: [definições e compatibilidade].
- Deduplicação/identidade: [qual chave representa evento, pedido ou pessoa].
- Nulos, zeros, estornos e ausência de eventos: [tratamento].
- Agregação permitida: [eixos aditivos, não aditivos e recomputação].

## Tempo e dimensões

- Data de referência: [evento, pagamento, captura etc.].
- Fuso/calendário: [regra e horário de corte].
- Janela e fechamento: [início inclusivo/fim exclusivo; período parcial].
- Dimensões permitidas: [cortes e relacionamentos].
- Histórico dimensional: [atributo atual ou vigente no evento].
- Atualização e cobertura: [condições de disponibilidade].

## Exemplo e validação

| Entrada ilustrativa | Resultado esperado | Explicação |
|---|---|---|
| [dados sintéticos mínimos] | [valor] | [regra aplicada] |

- Consulta/cálculo independente: [referência no projeto].
- Cortes e tolerância: [total, segmentos, período e motivo].
- Casos de borda: [denominador zero, atraso, cancelamento, grupos sobrepostos].
- Resultado e aceite: [data, evidência e aprovador].

## Comunicação

- Limitações de interpretação: [proxies, cobertura e causalidade].
- Consumidores afetados: [relatórios/aplicações].
- Política de mudança: [versão, transição e recálculo histórico].

Exemplo: ticket médio é receita elegível dividida por pedidos distintos elegíveis. Em fato de itens, média de receita por linha calcula valor médio do item, não ticket por pedido.
