# Documentação de modelo dbt — [nome]

Copie para o projeto. Transfira definições relevantes para propriedades do modelo/colunas no dbt e mantenha aqui decisões e operação. Consulte [documentação e lineage](../guias/documentacao-e-lineage.md).

## Identidade e contrato

- Nome, caminho e camada: [modelo; staging/intermediate/marts].
- Propósito e perguntas atendidas: [necessidade].
- Responsável e consumidores: [papéis e interfaces].
- Grão: **Cada linha representa [unidade]**.
- Chave única e regra de geração: [campos completos].
- Inputs e dependências: [sources/ref; origem externa relevante].
- Versão/data de revisão: [registro].

## Colunas críticas

| Coluna | Significado/origem | Tipo/unidade | Nulos/domínio | Derivação | Testes |
|---|---|---|---|---|---|
| [coluna] | [conceito e fonte] | [tipo] | [regra] | [cálculo] | [asserção] |

## Regras

- População, filtros e exclusões: [regras de negócio].
- Joins e cardinalidades: [campos, vigência e evidência].
- Deduplicação e desempate: [regra determinística].
- Datas, timezone e histórico: [semântica].
- Cancelamentos, estornos e unknowns: [comportamento].

## Materialização e processamento

- Materialização e justificativa: [view/table/ephemeral/incremental].
- Frequência, retenção e SLA acordado: [condições, sem promessa não validada].
- Se incremental: [chave, marcador, janela, atrasos, updates, deletes e política de schema].
- Backfill/full refresh: [quando usar, limites históricos, custo e validação].
- Engine/adaptador/dependências: [versões compatíveis].

## Validação e operação

| Verificação | Recorte/caso | Esperado/tolerância | Evidência | Resultado |
|---|---|---|---|---|
| [teste/reconciliação] | [intervalo/população] | [limite justificado] | [referência] | [registro] |

- Limitações e uso inadequado conhecido: [descrição].
- Falhas esperadas e responsável: [sintoma e ação].
- Procedimento de recuperação/reexecução: [referência ao runbook do projeto].
- Mudanças incompatíveis e transição: [consumidores, data e versão].

Revise com o [checklist dbt](../checklists/revisao-modelos-dbt.md).
