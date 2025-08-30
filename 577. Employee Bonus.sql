-- Write your MySQL query statement below
SELECT t.name, t.bonus
FROM (
    SELECT Employee.name, Bonus.bonus 
    FROM Employee
    LEFT JOIN Bonus
    ON Employee.empId = Bonus.empId ) AS t
WHERE t.bonus IS NULL OR t.bonus < 1000;