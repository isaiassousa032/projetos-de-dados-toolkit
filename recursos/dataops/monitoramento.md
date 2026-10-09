# Monitoramento

Monitore condições que importam ao consumidor. Status do job, disponibilidade, atualidade e validade do resultado são sinais diferentes.

## Definição de um sinal

Para cada condição, registre medida, janela, limite justificado, impacto, responsável e ação. Um pipeline diário pode exigir verificar lote completo antes do horário de consumo, além de registrar última execução.

| Condição | Evidência | Diagnóstico inicial |
|---|---|---|
| Falha de execução | Status e logs do componente | Dependência, acesso, sintaxe ou disponibilidade |
| Atraso | Última chegada e janela de consumo | Origem ou ingestão parou? |
| Cobertura incompleta | Contagem/partições contra expectativa | Lote parcial ou mudança de população? |
| Violação de qualidade | Regra, linhas afetadas e período | Origem, transformação ou definição mudou? |
| Custo/duração fora do padrão | Volume, varredura e tempo | Novo volume, join ou materialização? |

## Resposta a incidente

1. Identifique recorte, consumidores e gravidade.
2. Contenha resultado inválido ou sinalize incompletude conforme impacto.
3. Localize a primeira fronteira que diverge do esperado.
4. Corrija a causa e reexecute com segurança o intervalo afetado.
5. Reconcilie e confirme consumo antes de encerrar.
6. Registre causa, detecção, resolução e prevenção.

Evite alertas repetidos sem ação. Agrupe ocorrências correlacionadas e ajuste limites com evidência, sem ocultar falha recorrente. Em análises pontuais, uma verificação de atualização e cobertura no momento da entrega pode bastar; monitoramento contínuo depende de recorrência.

Veja [deploy e monitoramento](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md) e [qualidade compartilhada](../../compartilhado/guias/qualidade-de-dados.md).
