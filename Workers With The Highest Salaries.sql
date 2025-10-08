-- Management wants to analyze only employees with official job titles. Find the job titles of the employees with the highest salary. If multiple employees have the same highest salary, include all their job titles.

with t as
(select w.salary,w.worker_id,t.worker_title
from worker as w 
join title as t on w.worker_id=t.worker_ref_id)
select worker_title from
(select e.*, dense_rank() over(order by salary desc) as 'rnk' from t as e)x where x.rnk=1