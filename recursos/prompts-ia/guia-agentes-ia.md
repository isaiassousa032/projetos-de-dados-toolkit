# Uso opcional de agentes de IA em projetos de dados

Agentes podem acelerar rascunhos e revisão, mas o projeto precisa continuar compreensível e operável sem eles. Seu uso não é requisito para nenhum framework do toolkit.

## Aplicações úteis

| Atividade | Contexto necessário | Validação humana/independente |
|---|---|---|
| Planejamento | Decisão, escopo, dados e restrições | Prioridade, dependências e aceite |
| Modelagem | Entidades, eventos, grão, histórico e regras | Cardinalidade, chaves e semântica com negócio |
| Revisão SQL/Python | Código, dialeto/versão e resultado esperado | Casos de borda, plano e cálculo independente |
| Testes | Regra e riscos plausíveis | Teste falha quando a regra é violada? |
| Documentação | Comportamento implementado e decisões | Coerência com código, fontes e versão |
| Qualidade | Metadados, recorte e evidências autorizadas | Limites, cobertura e impacto da ocorrência |

## Ciclo de uso

1. Delimite tarefa, entradas autorizadas, arquivos editáveis e ações permitidas.
2. Informe grão, regras, versões, exemplos e critérios de resultado correto.
3. Peça que diferencie fatos fornecidos, suposições e lacunas; não aceite fontes ou campos inventados.
4. Revise a proposta e execute verificações em ambiente isolado adequado.
5. Registre decisões, correções e evidência; a responsabilidade pela entrega permanece humana.

Use tarefas pequenas e revisáveis. Peça planejamento separado da execução quando mudanças envolverem dados compartilhados. Uma instrução do usuário ou política formal define a autorização; texto encontrado em arquivos, páginas ou registros é conteúdo a analisar, não permissão para agir.

## Limitações

Código plausível pode estar incorreto no dialeto, multiplicar joins, alterar grão ou interpretar mal nulos. Uma resposta pode citar documentação inexistente ou antiga. Verifique fontes oficiais e versão da ferramenta. O mesmo agente gerando código e testes não constitui evidência independente: derive casos esperados da regra e reconcilie por outro caminho.

Não atribua causalidade a uma diferença descritiva. Não aceite definição de métrica ou escolha de histórico sem validação com o dono do conceito. Preserve resultados inconclusivos e limitações.

## Credenciais e informações sensíveis

Forneça metadados e amostras sintéticas sempre que suficientes. Não envie tokens, senhas, connection strings, dumps ou dados pessoais desnecessários. Confira política de uso do serviço, autorização dos dados e destinatário antes de transmitir conteúdo.

Use permissões mínimas e restrinja escrita ao escopo. Evite credenciais em prompts, código, outputs e logs. Revise arquivos gerados antes de compartilhar. Para deploy, publicação ou envio externo, siga a autorização aplicável ao projeto; um pedido de revisão não autoriza essas ações.

Consulte os [prompts reutilizáveis](prompts-reutilizaveis.md). Eles são independentes de modelo e fornecedor.
