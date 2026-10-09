# Camada semântica

A camada semântica centraliza definições de métricas e relações para diferentes consumidores. É **opcional**: marts bem documentados e poucos relatórios podem ser suficientes.

## Quando avaliar

Considere quando equipes calculam a mesma métrica de formas diferentes, várias ferramentas precisam compartilhar regras ou mudanças exigem manutenção repetida. Estime manutenção, compatibilidade dos consumidores e custo da solução antes de adotar.

Mantenha o [template de métrica](../templates/definicao-metricas-negocio.md) como contrato independente de ferramenta. Ele continua útil quando a semântica está em SQL ou BI.

## Contrato semântico

| Elemento | Decisão necessária |
|---|---|
| Entidades | Identificadores e cardinalidades que permitem relacionar modelos |
| Dimensões | Cortes permitidos e significado histórico |
| Tempo | Data da métrica, timezone, calendário e períodos incompletos |
| Medidas | Campos base, agregações e grão compatível |
| Métricas | Fórmula, população, filtros e tratamento de exceções |
| Governança | Dono, versão, aprovação e comunicação de mudança |

Receita líquida e quantidade de pedidos precisam compartilhar população quando formarem ticket médio. Contagem distinta não pode ser somada automaticamente entre grupos sobrepostos. Um saldo pode ser agregado entre contas em um instante, mas não somado entre dias.

## dbt Semantic Layer

Avalie o dbt Semantic Layer quando os recursos da engine/plataforma e as integrações de consumo atenderem ao projeto. A sintaxe e os recursos variam por versão; não copie uma configuração sem identificar o ambiente. A [documentação oficial de modelos semânticos](https://docs.getdbt.com/docs/build/semantic-models) é a referência para entidades, dimensões e definições compatíveis.

Este guia não impõe contratação ou uso de um fornecedor. Modelos físicos confiáveis, grão explícito e regras acordadas continuam necessários qualquer que seja a solução semântica.

## Validação antes do consumo

1. Calcule a métrica com SQL de referência sobre população e período fixos.
2. Compare total e cortes por dimensões autorizadas.
3. Verifique joins, duplicação, nulos, denominador zero e sobreposição de grupos.
4. Valide períodos incompletos, mudanças de atributo e escolha temporal em SCD2.
5. Obtenha aceite do dono da métrica e teste o consumidor real.

Se joins mudam o resultado, corrija modelagem ou caminho de relacionamento antes de liberar. Não use a camada semântica para esconder um grão inconsistente.

## Evolução

Mudança de definição exige versão, exemplos de antes/depois, impacto histórico e consumidores afetados. Defina transição e data de adoção. Consulte [documentação e lineage](documentacao-e-lineage.md).
