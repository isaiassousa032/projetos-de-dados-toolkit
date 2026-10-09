# Qualidade de dados

Qualidade é adequação ao uso pretendido. Investigue primeiro se os dados sustentam a pergunta e o nível de confiança necessário. O [diagnóstico original](guia-primeiras-perguntas.md) fornece perguntas iniciais; este guia organiza critérios e resposta.

| Dimensão | Verificação | Risco para a decisão |
|---|---|---|
| Completude | Campos críticos e população esperada estão presentes? | Ausências enviesam segmentos ou denominadores |
| Unicidade | Identificador é único no grão declarado? | Duplicações inflam contagens e somas |
| Validade | Tipos, domínios e datas são plausíveis para a regra? | Valores aceitos tecnicamente podem ser semanticamente inválidos |
| Consistência | Regras e relações concordam entre tabelas? | Joins e definições produzem resultados divergentes |
| Atualidade | Dados chegam dentro da janela necessária? | Decisão usa período incompleto ou atrasado |
| Exatidão | Há confronto com origem ou referência independente? | Dados coerentes internamente podem estar errados |

## Diagnóstico proporcional

1. Declare grão, chave e recorte. Conte linhas, chaves distintas e nulos críticos.
2. Verifique distribuição temporal, lacunas e cobertura da população.
3. Investigue duplicações, relações e significado das colunas usadas nas métricas.
4. Reconcilie contagens e medidas no mesmo período, filtro e corte de atualização.
5. Registre limitações, impacto sobre a pergunta e ação necessária.

Não remova outliers ou preencha nulos automaticamente. Um valor negativo pode representar estorno; ausência pode significar “não se aplica”. Consulte origem e regra antes de tratar. Registre o efeito da correção na população e na métrica.

## Registro de ocorrência

| Regra/achado | Evidência/recorte | Impacto | Ação | Responsável | Critério de resolução |
|---|---|---|---|---|---|
| [condição observada] | [consulta/amostra] | [decisão afetada] | [corrigir/limitar/bloquear] | [papel] | [resultado esperado] |

Uma ocorrência crítica pode impedir a entrega; uma limitação conhecida pode permitir resposta restrita, com aceite explícito. Defina tolerância pelo impacto e não por um percentual arbitrário.

## Aplicação aos frameworks

O Lite verifica os campos e recortes necessários para sua pergunta e registra limites no template. O Completo usa o diagnóstico antes de testar hipóteses. Analytics Engineering transforma regras recorrentes em [testes e verificações operacionais](../../analytics-engineering/guias/testes-e-qualidade.md), com responsáveis e resposta a falhas.

Uma execução bem-sucedida não demonstra cobertura, e totais iguais podem esconder diferenças que se compensam. Examine segmentos relevantes e a compatibilidade do grão antes de interpretar.
