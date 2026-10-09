# Git e versionamento

Versione código, regras, documentação e testes. Dados brutos volumosos, segredos e artefatos gerados devem seguir a política do projeto. Git registra alterações de arquivos; não restaura automaticamente o estado de um warehouse.

## Rotina de trabalho

1. Confira branch, estado local e mudanças pendentes antes de editar.
2. Faça mudanças pequenas e relacionadas a um problema concreto.
3. Revise o diff, os destinos de arquivos movidos e a documentação afetada.
4. Execute verificações apropriadas e registre evidências.
5. Faça commit e abra revisão conforme o fluxo autorizado da equipe/projeto.

Comandos de inspeção úteis:

```bash
git status --short
git diff --check
git diff
git diff --cached
git log --oneline -5
```

`git diff` cobre arquivos rastreados; arquivos novos ainda não adicionados precisam de revisão direta ou comparação externa. Em uma migração, use `git mv` para arquivos rastreados quando adequado, confira links e integridade antes de remover a origem. Para binários, compare hashes; para textos adaptados, registre mudanças e mantenha origem recuperável.

## Revisão de mudanças de dados

Explique problema, comportamento resultante, consumidores e validação. Uma revisão de SQL deve avaliar população, joins, grão, nulos e histórico, além de sintaxe. Diferencie mudança editorial de mudança de regra que altera métricas.

Evite misturar credenciais, ajustes de infraestrutura e alteração de método na mesma mudança sem relação clara. Não reescreva histórico compartilhado nem descarte trabalho local sem autorização.

Referência: [documentação oficial do Git](https://git-scm.com/doc). Consulte [CI/CD](ci-cd.md) e [convenções](../../compartilhado/guias/convencoes-nomenclatura-documentacao.md).
