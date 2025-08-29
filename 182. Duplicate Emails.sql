-- Write your MySQL query statement below
SELECT email as Email 
FROM (SELECT email, COUNT(email) as ct FROM Person GROUP BY email) as t 
WHERE t.ct > 1;
