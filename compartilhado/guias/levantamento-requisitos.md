# Levantamento de requisitos

Transforme uma pergunta em condições verificáveis de entrega. Use conversa com stakeholders e inspeção de fontes; não presuma que um nome de coluna corresponde à definição do negócio.

## Conversa orientadora

| Tema | Perguntas | Registro útil |
|---|---|---|
| Uso | Quem consome? Que ação depende da resposta? | Decisão, consumidor e aprovador |
| Significado | Qual população, métrica, período e comparação? | Definição e exemplo esperado |
| Fonte | Onde cada conceito é registrado? Há histórico? | Autoridade, cobertura e limitações |
| Atualização | Quando o consumidor precisa do dado? | Horário, atraso e período completo |
| Acesso | Quais dados podem ser usados e compartilhados? | Papéis, sensibilidade e restrições |
| Aceite | Como saber que a entrega atende? | Consulta, reconciliação ou cenário de uso |

## Procedimento

1. Identifique requisitos obrigatórios para a primeira entrega e desejáveis para evolução.
2. Confronte definições com a fonte: chaves, grão, estados, datas, exclusões e alterações.
3. Registre um exemplo para cada requisito crítico e quem valida o resultado.
4. Avalie lacunas, custo, prazo e acesso; renegocie o escopo quando necessário.
5. Obtenha concordância sobre o recorte e registre mudança posterior com efeito no aceite.

“Dados rápidos” é ambíguo. “Dados do dia anterior disponíveis até o horário acordado, com lote completo e reconciliação do recorte” permite verificação. Os limites precisam refletir necessidade real; este toolkit não define SLA universal.

## Escala da documentação

Em uma análise pontual, registre problema, fonte, pergunta, período e limitações no próprio template de análise. Em Analytics Engineering, use o [template de requisitos](../../analytics-engineering/templates/levantamento-requisitos.md) para consumidores, atualização e operação. Não crie dois registros com o mesmo conteúdo: faça referência ao registro principal do projeto.

Requisitos não terminam no início. Uma fonte que perde histórico ou muda semântica pode exigir rever pergunta, modelagem e métricas. Ligue essa decisão à [documentação](convencoes-nomenclatura-documentacao.md).
