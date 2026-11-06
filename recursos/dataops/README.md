# DataOps

Práticas para desenvolver, revisar e operar ativos de dados com confiança. Escale o processo ao risco: uma análise pontual precisa de rastreabilidade e validação; um pipeline recorrente precisa também de recuperação e monitoramento.

- [Git e versionamento](git-e-versionamento.md).
- [CI/CD e monitoramento](ci-cd-e-monitoramento.md).
- [Testes e automação](testes-e-automacao.md).
- [Documentação](documentacao.md).

O ciclo de referência é o Analytics Development Lifecycle (ADLC), da dbt Labs: planejar, desenvolver, testar, implantar, operar/observar e descobrir/analisar. O [whitepaper oficial](https://www.getdbt.com/resources/guides/the-analytics-development-lifecycle) não é redistribuído aqui.

```text
Planejar → Desenvolver → Testar → Implantar → Operar e observar → Descobrir e analisar
    ↑                                                                                │
    └────────────────────────────────────────────────────────────────────────────────┘
```

Este diretório não configura automações. Para detalhes dbt e evolução com Airflow, veja [deploy e monitoramento](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md).
