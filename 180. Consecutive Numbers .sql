select distinct num as ConsecutiveNums from
(select num ,lag (num ,1) over (order by id) as prev_num,
lead (num , 1) over (order by id) as next_num from Logs ) as cte 
where num = prev_num and num = next_num;