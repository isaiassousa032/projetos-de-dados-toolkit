# Ingestão idempotente

Ingestão é extrair da fonte e gravar na camada Bronze **sem transformar**. O objetivo é poder rodar quantas vezes precisar, para qualquer data, e obter sempre o mesmo resultado. Sem isso, toda falha vira uma limpeza manual.

## Os cinco requisitos

1. **Idempotente por partição.** A unidade de gravação é a partição por data de referência. Rodar a mesma data de novo sobrescreve a partição; nunca acrescenta.
2. **Escrita atômica.** Grave em arquivo temporário e renomeie ao final. Uma queda no meio não pode deixar um arquivo pela metade.
3. **Falha alta.** Resposta vazia, parcial ou com erro interrompe a execução. Não grave arquivo vazio e não avance nenhum marcador.
4. **Metadados de rastreio.** Toda linha leva a origem (`_source`) e o momento da ingestão (`_ingested_at`).
5. **Backfill por intervalo.** O script recebe `--start` e `--end`. A execução diária é só um backfill de um dia.

O [extract_example.py](../../template-projeto/src/ingestion/extract_example.py) do template aplica os cinco.

## Três datas diferentes

| Data | Significa | Uso |
|---|---|---|
| Referência | Quando o fato ocorreu | Chave da partição |
| Atualização | Quando a fonte revisou o registro | Detectar mudança |
| Ingestão | Quando você gravou | Metadado `_ingested_at` |

Particione pela data de referência e nunca pela de ingestão: é a referência que você reprocessa. Veja também as [decisões mínimas de arquitetura](../../analytics-engineering/guias/arquitetura-e-camadas.md).

## Completa, janela móvel ou marcador

- **Fonte pequena ou sem filtro por data:** carga completa a cada execução.
- **Fonte que revisa dados antigos (padrão para a maioria):** reprocesse uma janela móvel dos últimos *N* dias, com *N* igual ao maior atraso conhecido da fonte. Registre *N* na documentação.
- **Marcador de último registro:** só quando a janela for impraticável. Avance o marcador depois de gravar, nunca antes.

## Falhas de rede

Repita erros temporários (timeout, 429, 5xx) com espera crescente. Falhe de imediato em erros permanentes (400, 401, 404): repetir não resolve. Respeite o limite de taxa da fonte e, se ela informar o total de registros, compare com o que recebeu.

```python
import time


def with_retries(fn, retry_on=(ConnectionError, TimeoutError), attempts=3, base_delay=2.0):
    """Repete `fn` com espera exponencial só para erros temporários."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except retry_on:
            if attempt == attempts:
                raise
            time.sleep(base_delay * 2 ** (attempt - 1))
```

## Esquema que muda

A Bronze guarda como veio. Coluna nova entra sem quebrar nada. Coluna renomeada ou removida deve ser detectada nos testes da Silver, e nunca "consertada" na Bronze.

## Segredos

Chaves ficam em `.env` (fora do Git). Não imprima URLs com chave nos logs.

## Teste a ingestão

Três testes valem mais que qualquer outro:

1. Rodar a mesma data duas vezes mantém a contagem.
2. Um backfill de intervalo cria exatamente as partições esperadas.
3. Fonte vazia falha e não grava arquivo.

**Pronto para avançar:** os três testes passam e a camada Bronze pode ser apagada e recriada só com o script. Próximo passo: [arquitetura em camadas](arquitetura-medalhao.md).

[Voltar à Engenharia de Dados](../README.md).
