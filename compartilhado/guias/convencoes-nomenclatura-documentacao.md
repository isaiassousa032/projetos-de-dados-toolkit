# Convenções de nomenclatura e documentação

Use convenções para tornar os materiais fáceis de encontrar e manter. Respeite padrões existentes do projeto quando houver justificativa técnica.

## Nomes

| Objeto | Convenção | Exemplo |
|---|---|---|
| Documentos e diretórios | `kebab-case`, sem acentos no caminho | `modelagem-dimensional.md` |
| Índice de diretório | `README.md` | `analytics-engineering/README.md` |
| Modelos e colunas SQL/dbt | `snake_case`, nomes descritivos | `fct_itens_pedido`, `receita_liquida` |
| Staging | Prefixo por camada e origem, segundo padrão do projeto | `stg_comercial__itens_pedido` |
| Intermediate | Verbo/transformação reconhecível | `int_itens_pedido_elegiveis` |
| Marts dimensionais | `fct_` e `dim_` quando adotados | `dim_produto` |
| Decisões | Número e assunto | `adr-001-estrategia-de-carga.md` |

Termos como staging, intermediate, marts, sources, lineage e deploy permanecem em uso. Não use hífens nos nomes de modelos dbt apenas para reproduzir o padrão de documentos. Evite abreviações sem glossário e nomes que ocultem unidade ou data de referência.

## Estrutura de um documento útil

Comece por propósito e momento de uso. Registre procedimento, decisões, exemplos identificados e critério de validação. Templates devem explicar o preenchimento; campos em branco são parte do formulário, não ausência de conteúdo. Checklists precisam ter condição de aprovação e registro de evidência.

Exemplos fictícios devem dizer que são ilustrativos; exemplos reais devem citar contexto, versão e origem autorizada. Não declare projetos concluídos, resultados ou credenciais sem evidência.

## Links e manutenção

- Use links relativos a partir do arquivo atual, incluindo imagens.
- Ao mover um documento, atualize links de entrada e saída.
- Use títulos de link legíveis e evite links Obsidian em conteúdo destinado ao GitHub.
- Nas referências externas, identifique documentação oficial e data de consulta quando for relevante.
- Registre versão do projeto e ferramenta quando sintaxe ou comportamento dependerem delas.
- Centralize regra compartilhada e faça referência; repita somente contexto necessário ao uso independente.

## Segurança e evolução

Não inclua credenciais, tokens, connection strings ou dados pessoais nas amostras. Use nomes fictícios e entradas mínimas para explicar lógica. Mantenha código de projetos e artefatos operacionais em seus repositórios.

Altere método, exemplos e checklists na mesma revisão quando a mudança afetar os três. Confira links, conflitos de nomes e fontes. Consulte [documentação DataOps](../../recursos/dataops/documentacao.md).
