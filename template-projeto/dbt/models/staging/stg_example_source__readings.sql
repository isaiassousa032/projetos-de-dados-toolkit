-- Silver: renomeia, tipa e padroniza. Sem regra de negócio e sem joins.
select
    reading_id,
    cast(reference_date as date) as reference_date,
    station,
    cast(value as double) as reading_value,
    _source as source_name,
    _ingested_at as ingested_at
from {{ source('raw', 'example_source__readings') }}
