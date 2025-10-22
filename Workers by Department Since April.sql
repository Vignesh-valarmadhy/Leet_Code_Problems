-- Find the number of workers by department who joined on or after April 1, 2014.


-- Output the department name along with the corresponding number of workers.


-- Sort the results based on the number of workers in descending order.

WITH filtered_worker as (
select * 
from worker
where joining_date >= cast('2014-04-01' AS DATE) )

SELECT department,  
COUNT(worker_id) AS num_workers
FROM filtered_worker
GROUP BY department
ORDER BY num_workers DESC