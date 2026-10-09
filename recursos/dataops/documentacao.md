# Boas práticas de documentação

Documente o que outra pessoa precisa para usar, revisar e manter a entrega. A documentação deve representar a versão disponível, acompanhando mudanças de código e regras.

## Conteúdo por entrega

| Entrega | Registro essencial |
|---|---|
| Análise | Pergunta, fonte, recorte, método, evidências, conclusão e limites |
| Modelo | Propósito, grão, chave, regras, colunas, atualização e testes |
| Métrica | População, fórmula, tempo, unidade, agregação e responsável |
| Pipeline | Dependências, execução, resposta a falha, backfill e recuperação |
| Decisão | Contexto, alternativas, escolha, consequências e revisão |

Comece pelo uso e significado. Comente por que uma regra existe; SQL ou Python já mostram parte de como ela é executada. Não transforme README em inventário de ferramentas sem orientar o primeiro passo.

## Manutenção

1. Identifique o registro principal de cada regra e referencie-o nos consumidores.
2. Atualize exemplos e checklists junto da regra que mudou.
3. Verifique links após renomear ou mover arquivos.
4. Identifique exemplos reais ou fictícios e registre fontes externas confiáveis.
5. Remova instruções obsoletas após confirmar representação no substituto e possibilidade de recuperação.

Registre limitações e perguntas ainda não respondidas com impacto e responsável. Isso é diferente de preencher um diretório com texto vazio. Templates podem conter campos a preencher, desde que o propósito e as instruções sejam utilizáveis.

Consulte [convenções](../../compartilhado/guias/convencoes-nomenclatura-documentacao.md), [lineage](../../analytics-engineering/guias/documentacao-e-lineage.md) e [decisões arquiteturais](../../analytics-engineering/templates/decisoes-arquiteturais.md).
