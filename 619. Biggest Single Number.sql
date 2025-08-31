-- Write your MySQL query statement below
SELECT MAX(num) as num 
FROM (SELECT num, COUNT(num) as ct FROM MyNumbers GROUP BY num) AS t 
WHERE t.ct = 1;
