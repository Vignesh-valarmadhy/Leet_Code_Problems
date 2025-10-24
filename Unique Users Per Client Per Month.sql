-- # Write a query that returns the number of unique users per client for each month. Assume all events occur within the same year, so only month needs to be be in the output as a number from 1 to 12.

-- # Table
select client_id , 
        MONTH(time_id) as month,
        COUNT(DISTINCT user_id) as users_num 
        from fact_events
        group by client_id, month(time_id)
        order by month;