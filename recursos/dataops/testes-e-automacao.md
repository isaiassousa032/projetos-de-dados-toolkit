# Testes e automação

Automatize verificações que serão repetidas ou cuja falha compromete consumo. Um teste útil detecta um erro plausível com resultado esperado independente da implementação.

## Escolher verificações

- **Lógica:** casos sintéticos de cancelamento, nulo, denominador zero e fronteira temporal.
- **Estado dos dados:** chave, domínio, referência, cobertura e atualidade.
- **Reconciliação:** mesma métrica calculada a partir de origem ou método independente.
- **Integração:** contrato entre ingestão, transformação e consumidor.
- **Documentação:** destinos de links, âncoras e arquivos vazios.

Uma cópia da fórmula do código no teste pode reproduzir o mesmo erro. Comece por regras e amostras cujo resultado possa ser explicado manualmente. Para código Python, inclua DataFrames pequenos com grupos desiguais, índices duplicados ou tipos inesperados quando esses riscos forem pertinentes.

## Automatizar sem esconder falhas

Defina entrada, intervalo, saída, resultado esperado e resposta à falha. Preserve status e evidências de execução; retentativas devem respeitar idempotência. Separe falha transitória de erro de regra: repetir indefinidamente não corrige uma chave duplicada na origem.

Em dbt, consulte [testes e qualidade](../../analytics-engineering/guias/testes-e-qualidade.md). Em outros ambientes, consultas de asserção ou bibliotecas de teste podem cumprir a mesma responsabilidade.

## Validação desta biblioteca

O [validador local](validar-biblioteca.py) usa somente a biblioteca padrão do Python para conferir links Markdown locais, âncoras, arquivos vazios, nomes e duplicação de bytes. Ele não altera arquivos nem acessa a rede. A pasta `template-projeto/`, que contém código executável, fica fora das regras de nome e de arquivo vazio, mas seus links Markdown continuam validados.

Execute a partir da raiz:

```bash
python recursos/dataops/validar-biblioteca.py
```

O validador não substitui revisão editorial nem a execução de exemplos em um projeto real.
