# Modelagem dimensional — [processo]

Registre o desenho antes de implementar fatos e joins. Consulte o [guia de modelagem](../guias/modelagem-de-dados.md).

## Processo e grão

- Perguntas atendidas: [perguntas e consumidores].
- Tipo de fato: [transacional/snapshot periódico/acumulativo e motivo].
- Declaração do grão: **Cada linha representa [ocorrência/posição/intervalo]**.
- Chave no grão: [atributos completos, incluindo origem quando necessário].
- Evidência de unicidade: [consulta, recorte e resultado].
- Fonte de autoridade: [fonte e regra de precedência].

## Fato e medidas

| Medida | Significado/fórmula | Unidade | Agregação permitida | Nulos/exceções | Validação |
|---|---|---|---|---|---|
| [medida] | [regra] | [unidade] | [aditiva/semiaditiva/não aditiva e eixos] | [regra] | [referência] |

- Datas do processo e papéis da dimensão de tempo: [pedido, entrega, pagamento etc.].
- Cancelamentos, estornos e mudanças de estado: [tratamento e fonte].
- Totais que pertencem a outro grão: [como separar ou alocar sem duplicação].

## Dimensões e histórico

| Dimensão | Grão/chave natural | Chave substituta/versão | Atributos | Histórico por atributo | Conformidade |
|---|---|---|---|---|---|
| [dimensão] | [entidade/versão] | [identificador] | [campos] | [tipo 1/2 e motivo] | [processos que compartilham] |

- Vigência SCD2: [início inclusivo, fim exclusivo, versão corrente e fonte histórica].
- Associação temporal do fato: [data usada e regra para encontrar versão].
- Membro desconhecido e dimensão tardia: [linha, monitoramento e correção].
- Limite histórico: [o que não é possível reconstruir].

## Relacionamentos

| Origem → destino | Chaves de join | Cardinalidade esperada | Vigência/filtros | Evidência |
|---|---|---|---|---|
| [fato → dimensão] | [campos] | [N:1 esperado] | [condição] | [contagens antes/depois] |

- Muitos para muitos: [ponte/regra de alocação ou justificativa].
- Combinação entre fatos: [grão comum ou regra de associação].
- Consultas prioritárias: [como o desenho responde às perguntas].

## Implementação e revisão

- Tipos, precisão, schemas e constraints: [decisões da plataforma].
- Materialização e estratégia de carga: [decisão e justificativa].
- Testes: [unicidade, integridade, vigência, cardinalidade e reconciliação].
- Riscos, alternativas e aceite: [registro e responsáveis].
- Versão/data da revisão: [identificação].

Finalize com a [revisão de modelagem](../checklists/revisao-modelagem.md).
