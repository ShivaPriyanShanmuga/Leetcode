-- Write your MySQL query statement below
SELECT t.project_id, ROUND(AVG(t.experience_years), 2) AS average_years FROM (
    SELECT Project.project_id, Project.employee_id, Employee.experience_years
    FROM Project 
    JOIN Employee
    ON Employee.employee_id = Project.employee_id
) AS t
GROUP BY t.project_id;  