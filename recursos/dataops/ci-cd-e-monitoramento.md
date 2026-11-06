# CI/CD e monitoramento

CI verifica uma mudança antes de integrá-la. CD organiza a entrega/implantação de uma versão validada. Monitoramento observa, depois da entrega, as condições que importam ao consumidor. Revisão humana e promoção podem continuar explícitas conforme a política do projeto. Para dbt, veja [deploy e CI](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md); para Airflow, a [orquestração](../../engenharia-de-dados/guias/orquestracao-airflow.md).

## CI/CD

### Fluxo de referência

| Momento | Verificação | Evidência |
|---|---|---|
| Alteração local | Sintaxe, regras e exemplos controlados | Resultado e recorte usados |
| Revisão | Build/testes em destino isolado, contrato e impactos | Logs, testes e reconciliação |
| Promoção | Migração, backfill, permissões e recuperação | Versão e plano de deploy |
| Após entrega | Consumo, cobertura e qualidade | Smoke queries e aceite |

Para documentação, comece com links, arquivos vazios e nomes. Para SQL/dbt, valide dados representativos e não apenas compilação. Para Python, teste entradas e bordas das funções que transformam dados. Para BI, confira filtros, população e definição de medidas.

### Ambiente e seleção

Isolar destino é necessário para evitar que CI altere relações consumidas. Identifique versões, fontes, permissões e custo. Uma amostra pequena não reproduz todos os problemas de produção; escolha verificações adicionais pelo risco.

Em projetos grandes, validar só objetos alterados reduz duração, mas exige avaliar dependências e consumidores. Não exclua modelos pesados sem compreender o que deixa de ser validado.

### Recuperação

Defina como recuperar código e dados, não apenas retornar a um commit. Mudanças históricas ou perda de coluna podem exigir restauração e reprocessamento. Registre a versão entregue e o procedimento posterior para conferir os resultados.

Implemente automação no projeto quando o fluxo manual estiver compreendido. O [template-projeto](../../template-projeto/README.md) traz um workflow de exemplo no GitHub Actions; o restante do toolkit não pressupõe esse fornecedor.

## Monitoramento

Monitore condições que importam ao consumidor. Status do job, disponibilidade, atualidade e validade do resultado são sinais diferentes.

### Definição de um sinal

Para cada condição, registre medida, janela, limite justificado, impacto, responsável, canal e ação. Um pipeline diário pode exigir verificar lote completo antes do horário de consumo, além de registrar última execução.

| Condição | Evidência | Diagnóstico inicial |
|---|---|---|
| Falha de execução | Status e logs do componente | Dependência, acesso, sintaxe ou disponibilidade |
| Atraso | Última chegada e janela de consumo | Origem ou ingestão parou? |
| Cobertura incompleta | Contagem/partições contra expectativa | Lote parcial ou mudança de população? |
| Violação de qualidade | Regra, linhas afetadas e período | Origem, transformação ou definição mudou? |
| Consumo inesperado | Consultas e BI usando a versão esperada | Contrato ou transição quebrou? |
| Custo/duração fora do padrão | Volume, varredura e tempo | Novo volume, join ou materialização? |

### Resposta a incidente

1. Identifique recorte, consumidores e gravidade.
2. Contenha resultado inválido ou sinalize incompletude conforme impacto.
3. Localize a primeira fronteira que diverge do esperado.
4. Corrija a causa e reexecute com segurança o intervalo afetado.
5. Reconcilie e confirme consumo antes de encerrar.
6. Registre início, detecção, impacto, contenção, causa, resolução e prevenção.

Evite alertas repetidos sem ação. Agrupe ocorrências correlacionadas e ajuste limites com evidência, sem ocultar falha recorrente. Priorize o impacto ao consumidor. Em análises pontuais, uma verificação de atualização e cobertura no momento da entrega pode bastar; monitoramento contínuo depende de recorrência.

Veja também [deploy e monitoramento com dbt](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md) e [qualidade compartilhada](../../compartilhado/guias/qualidade-de-dados.md).
