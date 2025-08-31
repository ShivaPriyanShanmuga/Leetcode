-- Write your MySQL query statement below
SELECT t.employee_id 
FROM (
    SELECT Employees.employee_id, Employees.name, Salaries.salary
    FROM Employees
    LEFT JOIN Salaries
    ON Employees.employee_id = Salaries.employee_id
    UNION
    SELECT Salaries.employee_id, Employees.name, Salaries.salary
    FROM Salaries
    LEFT JOIN Employees
    ON Employees.employee_id = Salaries.employee_id
) AS t
WHERE t.name IS NULL OR t.salary IS NULL
ORDER BY t.employee_id;