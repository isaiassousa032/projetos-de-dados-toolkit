# Testes e automação

Automatize verificações que serão repetidas ou cuja falha compromete consumo. Um teste útil detecta um erro plausível com resultado esperado independente da implementação.

## Escolher verificações

- **Lógica:** casos sintéticos de cancelamento, nulo, denominador zero e fronteira temporal.
- **Estado dos dados:** chave, domínio, referência, cobertura e atualidade.
- **Reconciliação:** mesma métrica calculada a partir de origem ou método independente.
- **Integração:** contrato entre ingestão, transformação e consumidor.
- **Documentação:** destinos de links, arquivos vazios e integridade dos originais.

Uma cópia da fórmula do código no teste pode reproduzir o mesmo erro. Comece por regras e amostras cujo resultado possa ser explicado manualmente. Para código Python, inclua DataFrames pequenos com grupos desiguais, índices duplicados ou tipos inesperados quando esses riscos forem pertinentes.

## Automatizar sem esconder falhas

Defina entrada, intervalo, saída, resultado esperado e resposta à falha. Preserve status e evidências de execução; retentativas devem respeitar idempotência. Separe falha transitória de erro de regra: repetir indefinidamente não corrige uma chave duplicada na origem.

Em dbt, consulte [testes e qualidade](../../analytics-engineering/guias/testes-e-qualidade.md). Em outros ambientes, consultas de asserção ou bibliotecas de teste podem cumprir a mesma responsabilidade.

## Validação desta biblioteca

O [validador local](validar-biblioteca.py) usa somente a biblioteca padrão do Python para conferir links Markdown locais, âncoras, arquivos vazios, nomes, duplicação de bytes e hashes de origem. Ele não altera arquivos nem acessa a rede.

Execute a partir da raiz:

```bash
python recursos/dataops/validar-biblioteca.py
```

Confirme também o [relatório de migração](../referencias/relatorio-migracao.md). O validador não substitui revisão editorial, leitura visual dos binários ou execução de exemplos em um projeto real.
