# Arquitetura e separação de camadas

O desenho deve mostrar fluxo, responsabilidade e recuperação. Registre escolhas no [template de decisão](../templates/decisoes-arquiteturais.md); não adicione componentes sem um requisito que os justifique.

```text
Fontes → ingestão → raw → staging → intermediate (opcional) → marts
                                                              ↓
                                            SQL / BI / semântica (opcional)
```

## Fronteiras

| Camada/componente | Responsabilidade | Evitar |
|---|---|---|
| Fontes | Registrar operações/eventos e significados de origem | Presumir histórico que não existe |
| Ingestão | Extrair, carregar, capturar alterações e metadados | Avançar marcador antes de concluir lote |
| Raw | Preservar representação recebida e rastreabilidade conforme retenção | Aplicar regras de consumo sem registro |
| Staging | Renomear, tipar e padronizar cada origem | Misturar regras globais de vários processos |
| Intermediate | Integrar ou dividir lógica reutilizada/complexa | Criar camada obrigatória para consultas simples |
| Marts | Expor conceitos e grãos úteis ao consumo | Deixar interpretação de regra central em cada relatório |
| Consumo | Aplicar definições acordadas às perguntas | Recalcular a mesma métrica de formas divergentes |

Camadas lógicas não precisam ser todas tabelas físicas. Em dbt, sources descrevem entradas existentes e não fazem ingestão. ELT transforma depois da carga; ETL pode ser apropriado para restringir dados sensíveis ou adequar formatos antes de carregar.

## Decisões mínimas

- Fonte de autoridade por conceito e frequência de extração.
- Carga completa ou incremental/CDC; captura de atualizações e exclusões.
- Histórico e retenção necessários, com limite de reconstrução conhecido.
- Identificação de lote, origem, data do evento e data de chegada.
- Separação de dev, validação e produção por destinos e permissões.
- Acesso por papel, sensibilidade, limites de custo e responsável operacional.
- Idempotência, procedimento de backfill e recuperação de falha parcial.

## Exemplo de falha e resposta

Uma API fornece página incompleta durante uma carga. A ingestão não deve marcar o período como concluído. Guarde o estado do lote, repita a captura de forma segura e publique o resultado apenas após verificar cobertura e reconciliação. “Última execução bem-sucedida” não prova que todos os registros chegaram.

Especifique separadamente `ocorrido_em`, `atualizado_na_origem_em` e `carregado_em`. Um lote recente pode conter eventos antigos; usar somente data de evento como marcador perde alterações tardias.

## Escolha proporcional

Para uma primeira entrega local, uma fonte carregada e poucos modelos podem bastar. Para consumo recorrente, acrescente isolamento, registros de execução e resposta a falhas. Use Airflow quando dependências entre sistemas, concorrência e reprocessamento justificarem um orquestrador. Primeiro valide o pipeline; depois automatize.

Reveja o desenho ao adicionar fontes, elevar frequência ou mudar histórico. Consulte [materializações](materializacoes-e-incrementais.md) e [deploy](deploy-ci-cd-monitoramento.md).
