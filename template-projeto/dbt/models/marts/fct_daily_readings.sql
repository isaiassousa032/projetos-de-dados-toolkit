-- Gold: grão declarado = uma linha por estação por data de referência.
select
    reference_date,
    station,
    count(*) as readings_count,
    sum(reading_value) as total_value,
    avg(reading_value) as avg_value
from {{ ref('stg_example_source__readings') }}
group by reference_date, station
