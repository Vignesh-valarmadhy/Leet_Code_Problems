-- -- Calculates the difference between the highest salaries in the marketing and engineering departments. Output just the absolute difference in salaries.

-- db_employee
-- Preview
-- department_id:
-- bigint
-- first_name:
-- text
-- id:
-- bigint
-- last_name:
-- text
-- salary:
-- bigint
-- db_dept
-- Preview
-- department:
-- text
-- id:
-- bigint



select ABS(MAX(CASE
                    WHEN dept.department = 'marketing' THEN emp.salary 
                END) - Max(case 
                                when dept.department = 'engineering' THEN emp.salary 
                            END)) AS salary_difference 



From db_employee emp
JOIN db_dept dept ON emp.department_id = dept.id
WHERE dept.department IN ('marketing' , 'engineering');