# Deploy, CI/CD e monitoramento

Automatize uma entrega que já funciona e tem critérios de validação. Este guia descreve responsabilidades; arquivos de pipelines e infraestrutura pertencem ao repositório do projeto.

## CI proporcional ao risco

Em cada mudança, confira formatação/sintaxe, compilação, modelos afetados, testes e reconciliação em destino isolado. Um projeto pequeno pode validar todos os modelos; seleções por estado/defer exigem cobertura consciente das dependências e compatibilidade da versão.

Registre engine, adaptador, dependências e parâmetros usados. Amostras ajudam a testar lógica, mas podem omitir cardinalidades, atrasos e histórico; complemente com validação representativa. Revise código, documentação, contrato e consumidores na pull request.

No Core v1, `dbt build --target dev` é um exemplo de execução em destino de desenvolvimento, desde que o perfil esteja corretamente isolado. Freshness é uma verificação separada. [Build](https://docs.getdbt.com/reference/commands/build) e [source freshness](https://docs.getdbt.com/reference/commands/source) documentam as responsabilidades dos comandos; adapte-os à versão instalada.

## Plano de deploy

1. Identifique versão a promover, modelos e consumidores afetados.
2. Avalie mudança de schema, grão, semântica, histórico e permissões.
3. Planeje migração/backfill, janela, custo e sequência de transição.
4. Prepare recuperação de código **e dados**, com retenção/restauração compatíveis.
5. Promova segundo o processo autorizado do projeto, valide smoke queries e reconciliação.
6. Comunique atualização, limites e responsável por suporte; acompanhe o primeiro ciclo.

Reverter Git não restaura linhas alteradas. A recuperação pode exigir reconstrução, restauração ou reprocessamento. Não remova colunas ou modelos antes de verificar consumidores e prazo de transição.

## Orquestração opcional com Airflow

Comece validando ingestão e transformações com execução simples. Adote Airflow quando houver coordenação entre sistemas, retries, concorrência, backfills ou requisitos operacionais que justifiquem a manutenção.

Planeje tarefas por fronteira recuperável: confirmar ingestão → validar entrada → transformar/testar → verificar consumo. Use intervalos de dados explícitos e destinos determinísticos; uma retry deve produzir o mesmo estado esperado. Evite lógica pesada no carregamento do DAG e mantenha credenciais em conexões/segredos autorizados. [Boas práticas oficiais do Airflow](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html).

## Sinais e resposta

| Sinal | Pergunta | Resposta esperada |
|---|---|---|
| Execução | O job falhou ou excedeu duração? | Diagnosticar componente e retentar com segurança |
| Freshness | O dado chegou no horário de consumo? | Verificar origem, ingestão e atraso |
| Cobertura | O período/população está completo? | Reconciliação e contenção de resultado parcial |
| Qualidade | Regras críticas foram violadas? | Bloquear publicação afetada e corrigir causa |
| Consumo | Consultas/BI usam a versão esperada? | Validar contrato e transição |
| Custo | Varredura ou duração cresceu além do previsto? | Investigar volume, plano e materialização |

Defina limite, dono, canal e procedimento de resposta para cada alerta. Priorize impacto ao consumidor; não transforme todo desvio em notificação repetida. Registre incidentes com início, detecção, impacto, contenção, recuperação e ação preventiva.

Consulte [DataOps](../../recursos/dataops/README.md) e o [checklist de deploy e entrega](../checklists/deploy-entrega-final.md).
