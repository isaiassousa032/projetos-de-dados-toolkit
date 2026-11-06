-- Falha se houver mais de uma linha por estação e data (grão violado).
select reference_date, station, count(*) as rows_at_grain
from {{ ref('fct_daily_readings') }}
group by reference_date, station
having count(*) > 1
