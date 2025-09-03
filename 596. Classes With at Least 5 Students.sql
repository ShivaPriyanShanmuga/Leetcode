-- Write your MySQL query statement below
SELECT t.class
FROM (SELECT class, COUNT(class) AS ct FROM Courses GROUP BY class) AS t
WHERE t.ct >= 5;