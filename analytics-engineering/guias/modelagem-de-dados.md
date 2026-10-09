# Modelagem de dados

Use diferentes níveis de modelagem para resolver perguntas distintas. Consulte o [framework](framework-analytics-engineering.md) e registre o resultado no [template dimensional](../templates/modelagem-dimensional.md).

## Níveis e entregáveis

| Nível | Pergunta | Entrega | Validação |
|---|---|---|---|
| Conceitual | Quais entidades e eventos existem? | Relações, vocabulário e regras de negócio | Negócio reconhece cardinalidades e exceções |
| Lógico | Como organizar atributos e chaves? | Entidades/relações, dependências e grão | Chaves e relações confrontadas com fontes |
| Físico | Como implementar nesta plataforma? | Tipos, schemas, objetos, constraints e acesso | Precisão, integridade e consultas representativas |
| Dimensional | Como medir processos ao longo do tempo? | Fatos, dimensões, medidas e histórico | Agregações, joins e comparações coerentes |

Conceitual, lógico e físico também se aplicam ao desenho analítico. Não é obrigatório alterar bancos operacionais existentes. Normalização evita anomalias de escrita em sistemas transacionais; desnormalização em marts facilita leitura, desde que redundâncias sejam controladas.

## Procedimento prático

1. Escolha um processo e duas perguntas prioritárias. Identifique eventos, participantes e momentos.
2. Declare o grão antes de desenhar medidas e joins: uma linha por item de pedido identificado, por exemplo.
3. Liste chaves naturais, origem e necessidade de chave substituta. Um hash não corrige chave incompleta ou ambígua.
4. Classifique medidas: receita pode somar em cortes compatíveis; saldo não soma no tempo; ticket exige receita dividida por pedidos distintos.
5. Defina dimensões e histórico por atributo. Compartilhe dimensões conformadas quando processos usarem o mesmo conceito.
6. Implemente tipos e estratégias da plataforma; confira se constraints são impostas ou apenas informativas.
7. Valide grão, cardinalidade, integridade, reconciliação e resposta às perguntas.

## Fatos e histórico

| Estrutura | Grão ilustrativo | Cuidado |
|---|---|---|
| Fato transacional | Uma movimentação | Duplicações na ingestão alteram somas |
| Snapshot periódico | Produto, local e dia | Saldo é semiaditivo no tempo |
| Snapshot acumulativo | Uma solicitação com marcos | Mudanças atualizam a linha; não contar marcos como novas solicitações |
| Dimensão tipo 1 | Um cliente atual | Reclassifica eventos antigos pelo atributo atual |
| Dimensão tipo 2 | Uma versão de cliente | Join deve escolher a vigência válida no evento |

Em SCD2, use intervalos com início inclusivo e fim exclusivo e defina como representar a versão corrente. Teste ausência de sobreposição por entidade, chave única da versão e exatamente uma associação dimensional por fato. Preserve chave natural para rastreabilidade.

Para membros desconhecidos, crie uma linha correspondente na dimensão e acompanhe sua incidência. Quando a dimensão chegar depois, estabeleça como atualizar a chave do fato. Não atribua um cliente desconhecido a uma pessoa real.

## Falhas frequentes

- Juntar fatos de vendas e pagamentos por cliente pode multiplicar registros. Agregue ao grão comum ou modele uma associação explícita.
- Repetir total do pedido em cada item e somar aumenta receita. Aloque com regra validada ou mantenha medidas em fatos distintos.
- Usar `pedido_id + produto_id` como chave falha se o produto repetir no pedido. Use identificador do item ou posição estável validada.
- Somar taxas ou usar média simples de médias distorce pesos. Recalcule usando numeradores, denominadores e população compatíveis.

Veja o [exemplo de vendas](../exemplos/modelagem-vendas.md) e a [revisão de modelagem](../checklists/revisao-modelagem.md). Referência conceitual: [técnicas dimensionais do Kimball Group](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/).
