# Checklist — Deploy e entrega final

Use após o pipeline funcionar e antes de promover uma versão. Consulte [deploy, CI/CD e monitoramento](../guias/deploy-ci-cd-monitoramento.md).

- [ ] Critérios de aceite técnicos e de negócio foram demonstrados.
- [ ] Versão, dependências, destinos e escopo do deploy estão identificados.
- [ ] CI/revisão cobre alterações e consumidores afetados em ambiente isolado.
- [ ] Testes, reconciliação, freshness e cobertura passaram ou têm exceção justificada e aceita.
- [ ] Mudanças de schema, semântica e grão têm transição combinada.
- [ ] Migração/backfill possui custo, intervalo, procedimento e validação posterior.
- [ ] Recuperação de código e de dados é viável e está documentada.
- [ ] Credenciais são geridas pelo mecanismo autorizado, com acesso mínimo.
- [ ] Execução recorrente tem dependências, intervalos, idempotência e resposta a falhas definidos.
- [ ] Airflow, se adotado, tem necessidade justificada e não foi requisito para a primeira entrega.
- [ ] Alertas críticos possuem limite, dono, impacto e ação esperada.
- [ ] Modelos, métricas, lineage e runbook estão atualizados.
- [ ] Consumidores receberam orientações de uso, atualização, limitações e suporte.
- [ ] Primeiro ciclo após deploy foi verificado com smoke queries e reconciliação.
- [ ] Aceite final identifica versão, responsável e riscos remanescentes.

Marque o item do primeiro ciclo somente após observar a execução; os demais itens não comprovam essa condição antecipadamente.

Registro: [data, versão, responsável, evidências e resultado].
