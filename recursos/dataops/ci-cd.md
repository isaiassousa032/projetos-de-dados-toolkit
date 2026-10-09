# CI/CD para projetos de dados

CI verifica uma mudança antes de integrá-la. CD organiza a entrega/implantação de uma versão validada. Revisão humana e promoção podem continuar explícitas conforme a política do projeto.

## Fluxo de referência

| Momento | Verificação | Evidência |
|---|---|---|
| Alteração local | Sintaxe, regras e exemplos controlados | Resultado e recorte usados |
| Revisão | Build/testes em destino isolado, contrato e impactos | Logs, testes e reconciliação |
| Promoção | Migração, backfill, permissões e recuperação | Versão e plano de deploy |
| Após entrega | Consumo, cobertura e qualidade | Smoke queries e aceite |

Para documentação, comece com links, arquivos vazios e integridade dos materiais. Para SQL/dbt, valide dados representativos e não apenas compilação. Para Python, teste entradas e bordas das funções que transformam dados. Para BI, confira filtros, população e definição de medidas.

## Ambiente e seleção

Isolar destino é necessário para evitar que CI altere relações consumidas. Identifique versões, fontes, permissões e custo. Uma amostra pequena não reproduz todos os problemas de produção; escolha verificações adicionais pelo risco.

Em projetos grandes, validar só objetos alterados reduz duração, mas exige avaliar dependências e consumidores. Não exclua modelos pesados sem compreender o que deixa de ser validado. Para dbt, consulte [deploy e CI](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md).

## Recuperação

Defina como recuperar código e dados, não apenas retornar a um commit. Mudanças históricas ou perda de coluna podem exigir restauração e reprocessamento. Registre a versão entregue e o procedimento posterior para conferir os resultados.

Implemente automação no projeto quando o fluxo manual estiver compreendido. Uma ferramenta possível é [GitHub Actions](https://docs.github.com/en/actions); o toolkit não inclui configuração de workflow nem pressupõe esse fornecedor.
