-- Find the number of employees working in the Admin department that joined in April or later, in any year.
select count(worker_id)
from worker
where department = 'Admin' and month(joining_date) >= 4;