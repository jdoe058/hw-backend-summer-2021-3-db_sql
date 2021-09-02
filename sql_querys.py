# INFO
# Вывести топ 5 самых коротких по длительности перелетов
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
SELECT flight_no, (scheduled_arrival - scheduled_departure) as duration FROM flights order by duration limit 5;
"""
#  flight_no | duration 
# -----------+----------
#  PG0148    | 00:25:00
#  PG0039    | 00:25:00
#  PG0040    | 00:25:00
#  PG0014    | 00:25:00
#  PG0149    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 100
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_2_QUERY = """
select * from (select flight_no, count(flight_id) as count from flights
group by flight_no) as fl
where count < 50
order by count desc
limit 3;
"""

#  flight_no | count 
# -----------+-------
#  PG0611    |   396
#  PG0201    |   396
#  PG0303    |   396


# INFO
# Вывести число перелетов внутри одной таймзоны 
# Нузно вывести 1 значение в колонке count
TASK_3_QUERY = """
"""
#  count  
# --------
#  109185

