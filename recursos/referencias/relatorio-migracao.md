# Relatório de diagnóstico, migração e validação

Implementação realizada em 09/10/2026. Repositório lógico: **data-project-toolkit**. O checkout local permanece em `projetos-de-dados-toolkit`, preservando a localização do workspace e a configuração Git existente.

## Diagnóstico antes das alterações

- Não foi encontrado `AGENTS.md` no workspace, nos diretórios ancestrais verificados ou dentro dos ZIPs de origem.
- Os frameworks estavam disponíveis em dois ZIPs, com 5 entradas no Lite e 7 no Completo. Os arquivos ativos já estavam em parte organizados nas quatro áreas; a comparação não encontrou divergências substantivas, somente diferenças de finais de linha.
- O template Word Lite não consta do ZIP Lite: era um material adicional do workspace, com campo de processo de negócio, preservado como variante útil.
- O README principal estava vazio; Analytics Engineering possuía quatro `.gitkeep` vazios e nenhum conteúdo metodológico.
- Havia três PDFs na raiz, uma imagem ADLC com nome fora da convenção, links antigos para `modelos/`, referências Obsidian e um fragmento final repetido/truncado no guia Completo.
- Os READMEs de exemplos não continham casos concluídos; suas árvores eram orientações. A redação foi ajustada para não afirmar a existência de projetos reais.
- O Git central estava na branch `main`, sem commits e sem arquivos rastreados. A revisão final detectou `.git` embutidos em Lite e Completo, com históricos locais. Eles foram preservados integralmente e retirados das pastas ativas para evitar gitlinks. Nenhum commit ou histórico foi reescrito.

## Estrutura final

```text
data-project-toolkit/
├── README.md
├── analise-de-dados/
│   ├── README.md
│   ├── lite/
│   │   ├── README.md
│   │   ├── guias/
│   │   ├── templates/
│   │   ├── checklists/
│   │   └── imagens/
│   └── completo/
│       ├── README.md
│       ├── guias/
│       ├── templates/
│       └── exemplos/
├── analytics-engineering/
│   ├── README.md
│   ├── guias/
│   ├── templates/
│   ├── checklists/
│   └── exemplos/
├── compartilhado/
│   ├── README.md
│   ├── guias/
│   └── templates/
└── recursos/
    ├── README.md
    ├── dataops/
    │   └── imagens/
    ├── ferramentas/
    ├── prompts-ia/
    └── referencias/
        ├── materiais/
        └── originais/
```

Não foi criada pasta de checklists no Completo: os checklists originais já estão no guia principal. O Lite preserva seus cinco passos e utiliza apoio compartilhado apenas quando necessário.

## Arquivos originais preservados e destinos

A tabela cobre todas as entradas dos ZIPs, inclusive materiais já organizados antes desta execução. Nenhum foi substituído com base apenas no nome. Os originais íntegros permanecem nos ZIPs para recuperação.

| Origem/entrada | Destino ativo | Tratamento |
|---|---|---|
| `framework-analise-de-dados-lite-main.zip/README.md` | [analise-de-dados/lite/README.md](../../analise-de-dados/lite/README.md) | Navegação/redação adaptada; original no ZIP |
| `framework-analise-de-dados-lite-main.zip/checklist-projeto-curto.md` | [analise-de-dados/lite/checklists/checklist-projeto-curto.md](../../analise-de-dados/lite/checklists/checklist-projeto-curto.md) | Preservado sem alteração |
| `framework-analise-de-dados-lite-main.zip/framework-lite.md` | [analise-de-dados/lite/guias/framework-lite.md](../../analise-de-dados/lite/guias/framework-lite.md) | Preservado; apenas finais de linha diferentes no workspace |
| `framework-analise-de-dados-lite-main.zip/imagens/diagrama-fluxo-de-dados.png` | [analise-de-dados/lite/imagens/diagrama-fluxo-de-dados.png](../../analise-de-dados/lite/imagens/diagrama-fluxo-de-dados.png) | Binário preservado byte a byte |
| `framework-analise-de-dados-lite-main.zip/template-analise-lite.md` | [analise-de-dados/lite/templates/template-analise-lite.md](../../analise-de-dados/lite/templates/template-analise-lite.md) | Preservado; apenas finais de linha diferentes no workspace |
| `framework-analise-de-dados-main.zip/README.md` | [analise-de-dados/completo/README.md](../../analise-de-dados/completo/README.md) | Navegação/redação adaptada; original no ZIP |
| `framework-analise-de-dados-main.zip/exemplos/README.md` | [analise-de-dados/completo/exemplos/README.md](../../analise-de-dados/completo/exemplos/README.md) | Navegação/redação adaptada; original no ZIP |
| `framework-analise-de-dados-main.zip/guias/framework-analise-de-dados.md` | [analise-de-dados/completo/guias/framework-analise-de-dados.md](../../analise-de-dados/completo/guias/framework-analise-de-dados.md) | Navegação/redação adaptada; original no ZIP |
| `framework-analise-de-dados-main.zip/guias/guia-primeiras-perguntas.md.md` | [compartilhado/guias/guia-primeiras-perguntas.md](../../compartilhado/guias/guia-primeiras-perguntas.md) | Navegação/redação adaptada; original no ZIP |
| `framework-analise-de-dados-main.zip/templates/template-diagnostico-inicial.docx` | [analise-de-dados/completo/templates/template-diagnostico-inicial.docx](../../analise-de-dados/completo/templates/template-diagnostico-inicial.docx) | Binário preservado byte a byte |
| `framework-analise-de-dados-main.zip/templates/template-framework-analise.docx` | [analise-de-dados/completo/templates/template-framework-analise.docx](../../analise-de-dados/completo/templates/template-framework-analise.docx) | Binário preservado byte a byte |
| `framework-analise-de-dados-main.zip/templates/template-resumo-executivo.docx` | [analise-de-dados/completo/templates/template-resumo-executivo.docx](../../analise-de-dados/completo/templates/template-resumo-executivo.docx) | Binário preservado byte a byte |

Material adicional preservado: [analise-de-dados/lite/templates/template-analise-lite.docx](../../analise-de-dados/lite/templates/template-analise-lite.docx). A versão Word não foi convertida nem sobrescrita pela versão Markdown.

## Arquivos movidos ou renomeados

| Caminho inicial | Caminho final |
|---|---|
| `framework-analise-de-dados-main.zip` | [recursos/referencias/originais/framework-analise-de-dados-main.zip](originais/framework-analise-de-dados-main.zip) |
| `framework-analise-de-dados-lite-main.zip` | [recursos/referencias/originais/framework-analise-de-dados-lite-main.zip](originais/framework-analise-de-dados-lite-main.zip) |
| `GUIA_GERAL_ANALYTICS_ENGINEERING.pdf` | [recursos/referencias/materiais/guia-geral-analytics-engineering.pdf](materiais/guia-geral-analytics-engineering.pdf) |
| `dbt Fundamentals - Datacamp.pdf` | [recursos/referencias/materiais/dbt-fundamentals-datacamp.pdf](materiais/dbt-fundamentals-datacamp.pdf) |
| `The Analytics Development Lifecycle.pdf` | [recursos/referencias/materiais/the-analytics-development-lifecycle.pdf](materiais/the-analytics-development-lifecycle.pdf) |
| `recursos/dataops/imagens/Ciclo de Vida Analítico ADLC.png` | [recursos/dataops/imagens/ciclo-de-vida-analitico-adlc.png](../dataops/imagens/ciclo-de-vida-analitico-adlc.png) |

A cópia para cada destino foi comparada por SHA-256 antes da remoção do caminho inicial. Os bytes continuam preservados no destino.

## Preservação dos históricos Git

Os diretórios `.git` internos foram arquivados antes de qualquer movimentação, com teste CRC e comparação SHA-256 de cada arquivo. Após essa verificação, foram renomeados e movidos para uma cópia temporária fora da biblioteca; os ZIPs permanentes são a recuperação durável. O `.git` principal permaneceu no lugar. A movimentação dos metadados exigiu execução fora do sandbox devido à proteção de acesso; a revisão automática autorizou o escopo específico. Nenhuma configuração foi editada, nenhum commit foi criado e nenhum histórico foi reescrito.

- Completo: HEAD `ae6878879d843a424b5e2245ed3efbe5383182cd`, 37 arquivos de metadados.
- Lite: HEAD `f9b7358ed600c19e747567943a443867e2b4ba20`, 40 arquivos de metadados.
- Recuperação: extrair conteúdo e ZIP de metadados correspondentes em diretório separado, conforme o [índice de referências](README.md).

## Consolidações e correções

- O guia original `guia-primeiras-perguntas.md.md` está centralizado em `compartilhado/guias/guia-primeiras-perguntas.md`. A extensão já estava corrigida no workspace; os links e notas técnicas foram adaptados nesta execução.
- Links para `modelos/modelo-*.docx` foram corrigidos para os templates existentes. Referências Obsidian foram convertidas para links relativos ou rótulos nos exemplos de texto.
- Foram removidos somente os quatro `.gitkeep` vazios, cujas pastas receberam conteúdo útil, e o fragmento textual final repetido/truncado do guia Completo.
- Os checklists e o template de nota originais do Completo continuam no guia, evitando duplicação em novos arquivos.
- Os ZIPs preservam as versões originais; são cópias de recuperação intencionais, não guias ativos redundantes.
- O README principal recebeu conteúdo. Os READMEs de Lite, Completo e exemplos receberam navegação/correções; os dois guias originais do Completo/compartilhado receberam notas técnicas explícitas, sem substituir o método.

## Arquivos novos

Foram criados **47 arquivos** além dos materiais previamente existentes e dos destinos de movimentação. A lista inclui este relatório, o manifesto e o validador. Campos de templates são formulários utilizáveis, não documentos vazios.

- [analise-de-dados/README.md](../../analise-de-dados/README.md).
- [analise-de-dados/completo/exemplos/analise-receita-por-canal.md](../../analise-de-dados/completo/exemplos/analise-receita-por-canal.md).
- [analytics-engineering/README.md](../../analytics-engineering/README.md).
- [analytics-engineering/checklists/deploy-entrega-final.md](../../analytics-engineering/checklists/deploy-entrega-final.md).
- [analytics-engineering/checklists/inicio-projeto.md](../../analytics-engineering/checklists/inicio-projeto.md).
- [analytics-engineering/checklists/qualidade-dados.md](../../analytics-engineering/checklists/qualidade-dados.md).
- [analytics-engineering/checklists/revisao-modelagem.md](../../analytics-engineering/checklists/revisao-modelagem.md).
- [analytics-engineering/checklists/revisao-modelos-dbt.md](../../analytics-engineering/checklists/revisao-modelos-dbt.md).
- [analytics-engineering/exemplos/consultas-analiticas.md](../../analytics-engineering/exemplos/consultas-analiticas.md).
- [analytics-engineering/exemplos/modelagem-vendas.md](../../analytics-engineering/exemplos/modelagem-vendas.md).
- [analytics-engineering/exemplos/trechos-dbt.md](../../analytics-engineering/exemplos/trechos-dbt.md).
- [analytics-engineering/guias/arquitetura-e-camadas.md](../../analytics-engineering/guias/arquitetura-e-camadas.md).
- [analytics-engineering/guias/boas-praticas-dbt.md](../../analytics-engineering/guias/boas-praticas-dbt.md).
- [analytics-engineering/guias/camada-semantica.md](../../analytics-engineering/guias/camada-semantica.md).
- [analytics-engineering/guias/deploy-ci-cd-monitoramento.md](../../analytics-engineering/guias/deploy-ci-cd-monitoramento.md).
- [analytics-engineering/guias/documentacao-e-lineage.md](../../analytics-engineering/guias/documentacao-e-lineage.md).
- [analytics-engineering/guias/framework-analytics-engineering.md](../../analytics-engineering/guias/framework-analytics-engineering.md).
- [analytics-engineering/guias/materializacoes-e-incrementais.md](../../analytics-engineering/guias/materializacoes-e-incrementais.md).
- [analytics-engineering/guias/modelagem-de-dados.md](../../analytics-engineering/guias/modelagem-de-dados.md).
- [analytics-engineering/guias/testes-e-qualidade.md](../../analytics-engineering/guias/testes-e-qualidade.md).
- [analytics-engineering/templates/decisoes-arquiteturais.md](../../analytics-engineering/templates/decisoes-arquiteturais.md).
- [analytics-engineering/templates/definicao-metricas-negocio.md](../../analytics-engineering/templates/definicao-metricas-negocio.md).
- [analytics-engineering/templates/documentacao-modelos-dbt.md](../../analytics-engineering/templates/documentacao-modelos-dbt.md).
- [analytics-engineering/templates/levantamento-requisitos.md](../../analytics-engineering/templates/levantamento-requisitos.md).
- [analytics-engineering/templates/modelagem-dimensional.md](../../analytics-engineering/templates/modelagem-dimensional.md).
- [compartilhado/README.md](../../compartilhado/README.md).
- [compartilhado/guias/convencoes-nomenclatura-documentacao.md](../../compartilhado/guias/convencoes-nomenclatura-documentacao.md).
- [compartilhado/guias/definicao-problema-negocio.md](../../compartilhado/guias/definicao-problema-negocio.md).
- [compartilhado/guias/levantamento-requisitos.md](../../compartilhado/guias/levantamento-requisitos.md).
- [compartilhado/guias/qualidade-de-dados.md](../../compartilhado/guias/qualidade-de-dados.md).
- [compartilhado/templates/descricao-problema-negocio.md](../../compartilhado/templates/descricao-problema-negocio.md).
- [recursos/README.md](../README.md).
- [recursos/dataops/README.md](../dataops/README.md).
- [recursos/dataops/ci-cd.md](../dataops/ci-cd.md).
- [recursos/dataops/documentacao.md](../dataops/documentacao.md).
- [recursos/dataops/git-e-versionamento.md](../dataops/git-e-versionamento.md).
- [recursos/dataops/monitoramento.md](../dataops/monitoramento.md).
- [recursos/dataops/testes-e-automacao.md](../dataops/testes-e-automacao.md).
- [recursos/dataops/validar-biblioteca.py](../dataops/validar-biblioteca.py).
- [recursos/ferramentas/README.md](../ferramentas/README.md).
- [recursos/prompts-ia/guia-agentes-ia.md](../prompts-ia/guia-agentes-ia.md).
- [recursos/prompts-ia/prompts-reutilizaveis.md](../prompts-ia/prompts-reutilizaveis.md).
- [recursos/referencias/README.md](README.md).
- [recursos/referencias/manifesto-migracao.json](manifesto-migracao.json).
- [recursos/referencias/relatorio-migracao.md](relatorio-migracao.md).
- [recursos/referencias/originais/framework-completo-metadados-git.zip](originais/framework-completo-metadados-git.zip).
- [recursos/referencias/originais/framework-lite-metadados-git.zip](originais/framework-lite-metadados-git.zip).

## Arquivos existentes atualizados

- [README.md](../../README.md).
- [analise-de-dados/completo/README.md](../../analise-de-dados/completo/README.md).
- [analise-de-dados/completo/exemplos/README.md](../../analise-de-dados/completo/exemplos/README.md).
- [analise-de-dados/completo/guias/framework-analise-de-dados.md](../../analise-de-dados/completo/guias/framework-analise-de-dados.md).
- [analise-de-dados/lite/README.md](../../analise-de-dados/lite/README.md).
- [compartilhado/guias/guia-primeiras-perguntas.md](../../compartilhado/guias/guia-primeiras-perguntas.md).

## Validação

A execução e os resultados finais estão registrados abaixo. O [validador](../dataops/validar-biblioteca.py) permite repetir verificações locais sem rede ou escrita. O [manifesto](manifesto-migracao.json) guarda o estado inicial, hashes das entradas originais e os movimentos.

| Verificação | Resultado |
|---|---|
| Estrutura | 67 arquivos, 52 Markdown; quatro áreas principais preenchidas; nenhum diretório vazio |
| Links internos | 314 links locais verificados, incluindo âncoras e capitalização; zero destinos quebrados detectados |
| Origens | 12 entradas dos ZIPs conferidas e presentes no destino; ZIPs originais preservados |
| Binários preexistentes | 11 arquivos com SHA-256 idêntico ao estado inicial: 4 DOCX, 3 PDF, 2 PNG e 2 ZIP |
| Históricos Git | 77 metadados preservados e verificados nos dois ZIPs; `git fsck --full` aprovado; zero repositórios embutidos ativos |
| DOCX e ZIP | Integridade CRC aprovada; XML principal dos quatro documentos Word legível |
| PDFs | Três arquivos reabertos e texto das 68 páginas extraído; um aviso de tabela Xref foi tratado pelo leitor sem impedir leitura, e o arquivo permaneceu byte a byte intacto |
| Imagens | Duas PNGs decodificadas/verificadas sem erro, com hashes preservados |
| Exemplos SQL | Quatro consultas executadas em SQLite em memória sobre amostra fictícia, adaptando somente literal DATE; receita 220, dois pedidos, ticket 110 e categorias 140/80 |
| Casos negativos SQL | Duplicação de dimensão e de item detectadas pelas consultas de validação |
| Nomes e marcadores | Nomes de arquivos/diretórios ativos conforme convenção; zero arquivos vazios e zero documentos substituídos por marcadores |
| Duplicação | Nenhuma duplicação de bytes entre arquivos ativos; ZIPs de recuperação contêm intencionalmente os originais |
| Git central | `git diff --check` sem apontamentos; 67 arquivos não rastreados individualmente; nenhuma alteração staged, commit ou push |

A comparação de origem foi feita por hash para binários e por leitura/diff para Markdown adaptado. Como o Git central ainda não possui arquivos rastreados nem commits, o diff Git não representa toda a entrega; foram usadas inspeção direta e comparação com o estado inicial registrado no manifesto. Nenhuma configuração externa, infraestrutura, credencial ou automação foi editada.

Os blocos YAML didáticos foram revisados contra a documentação oficial, mas não houve validação com parser YAML nem execução dbt: esses pacotes não estavam disponíveis no runtime e nenhuma dependência foi instalada. A equivalência SQL verificada em SQLite não comprova compatibilidade com todos os dialetos. Os binários não tiveram conteúdo/layout alterado; a migração foi validada por hashes e abertura estrutural, sem conversão ou nova renderização.


## Pendências e limites

- Não há pendência de migração dos materiais disponíveis: ambos os ZIPs foram acessados integralmente e suas 12 entradas têm destino ativo.
- Os ZIPs de conteúdo não traziam históricos Git, mas os dois `.git` encontrados no workspace foram preservados em ZIPs próprios, com 77 arquivos de metadados verificados. As cópias recuperáveis passaram em `git fsck --full`. Não há histórico pendente de preservação entre os materiais locais encontrados.
- Não foram fornecidos casos reais preenchidos. Os exemplos novos estão identificados como fictícios/ilustrativos.
- O nome local da pasta foi mantido; eventual nome de repositório remoto deve ser definido pelo proprietário. Nenhum remoto foi criado ou renomeado.
- Os livros referenciados não foram fornecidos integralmente. Suas identificações foram conferidas em páginas oficiais; não se declara leitura integral deles.
- Antes de publicar o acervo de terceiros, confirme direitos de redistribuição de PDFs/imagem. Nenhuma licença foi inventada.
- Os trechos SQL/dbt são referências didáticas; não houve deploy nem execução contra DW ou projeto dbt real. A validação desta entrega é da biblioteca e dos exemplos controlados.

## Melhorias futuras — não implementadas

- Incorporar casos reais preenchidos e sanitizados, com evidências e permissão de compartilhamento.
- Executar os exemplos em uma stack escolhida no repositório de um projeto e registrar compatibilidade por engine/adaptador.
- Integrar o validador a CI quando o fluxo Git e a hospedagem forem definidos; nenhuma automação foi criada nesta tarefa.
- Rever referências técnicas periodicamente e registrar decisões de evolução dos métodos.
- Definir licença própria e separar eventuais materiais de terceiros que não possam ser redistribuídos.
