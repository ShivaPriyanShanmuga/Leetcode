-- Write your MySQL query statement below
SELECT actor_id, director_id
FROM (
    SELECT actor_id, director_id, COUNT(timestamp) AS ct
    FROM ActorDirector
    GROUP BY actor_id, director_id
    ) AS t
WHERE t.ct >= 3;