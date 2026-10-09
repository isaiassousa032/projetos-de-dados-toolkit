# Prompts reutilizáveis

Substitua campos entre colchetes por contexto autorizado. Remova credenciais e dados sensíveis; prefira amostras sintéticas. Use o [guia de agentes](guia-agentes-ia.md) para validar resultados.

## Planejamento e decomposição

```text
Objetivo de negócio: [decisão e pergunta]. Dados disponíveis: [fontes, grão,
cobertura e limites]. Escopo: [incluído/excluído]. Entrega: [resultado].
Decomponha em tarefas pequenas, dependências, entregáveis e critérios de aceite.
Separe fatos, suposições e perguntas abertas. Priorize uma primeira entrega útil.
Não exija Airflow, camada semântica ou nova infraestrutura sem requisito.
Não execute ações nem altere arquivos nesta etapa.
```

## Apoio à modelagem

```text
Domínio e regras confirmadas: [descrição]. Fontes: [entidades, chaves e exemplos
sintéticos]. Perguntas: [prioridades]. Histórico disponível: [limites].
Proponha conceitos, relações, grão dos fatos, dimensões e medidas.
Identifique riscos de cardinalidade, chaves incompletas, SCD2 e dupla contagem.
Justifique alternativas e liste o que precisa de validação do negócio.
Não invente histórico ou campos ausentes. Entregue descrição revisável e casos
de teste com resultados explicáveis manualmente.
```

## Revisão de SQL

```text
Dialeto e versão: [ambiente]. Contrato: [pergunta, população, grão, métricas,
filtros, timezone e histórico]. SQL: [código sem segredos].
Revise correção de joins, agregações, nulos, duplicações e intervalos temporais.
Para cada problema, mostre uma entrada sintética que revela o erro e o resultado
esperado. Separe correção de performance. Não altere a definição de negócio.
Informe incertezas e como validar. Não execute consultas em produção.
```

## Revisão de Python

```text
Versões e bibliotecas: [ambiente]. Entrada/saída esperadas: [schema e grão].
Regras: [definição]. Código: [trecho].
Revise tipos, merges, índices, groupby, valores ausentes e mutações inesperadas.
Use exemplos sintéticos pequenos com grupos desiguais e duplicações relevantes.
Explique defeitos reproduzíveis, correção mínima e validação independente.
Não instale dependências nem processe dados externos sem autorização.
```

## Geração e revisão de testes

```text
Regra de negócio: [definição]. Riscos: [cenários]. Grão/chaves: [contrato].
Crie casos positivos e negativos, bordas e resultados esperados a partir da regra.
Cubra [reexecução, atraso, exclusão, nulos, denominador zero] quando aplicável.
Não copie a implementação como único oráculo. Explique que falha cada teste
detecta e proponha reconciliação com uma referência independente.
```

## Documentação técnica

```text
Use apenas estes fatos: [modelo, propósito, grão, colunas, regras, fontes,
atualização, testes e limitações]. Produza documentação em português brasileiro
com links relativos e nomes compatíveis com o projeto.
Explique significado e uso. Não invente SLAs, fontes, resultados ou credenciais.
Liste separadamente lacunas que impedem documentar uma regra com precisão.
```

## Revisão de qualidade

```text
Pergunta e decisão: [contexto]. Evidências autorizadas: [contagens, períodos,
resultados de testes, reconciliação e metadados].
Avalie grão, cobertura, atualidade, nulos, duplicação, joins e tolerâncias.
Separe problemas comprovados de riscos ainda não verificados.
Indique impacto na conclusão, verificação necessária e prioridade de resposta.
Não conclua causalidade nem adequação de toda a base a partir de amostra parcial.
```

Após cada resposta, confira o contrato do projeto, reproduza exemplos e registre o resultado. Propostas de alteração precisam continuar dentro do escopo autorizado.
