-- Compare each employee's salary with the average salary of the corresponding department.
-- Output the department, first name, and salary of employees along with the average salary of that department.

-- Table
-- employee

select a.department, first_name , salary, avg_salary from employee a
left join 
(select department, avg(salary) as avg_salary 
from employee
group by department ) b

on a.department = b.department