/* Write your PL/SQL query statement below */

SELECT actor_id, director_id
FROM (
    SELECT actor_id, director_id, COUNT(1)
    FROM ActorDirector
    GROUP BY actor_id, director_id
    HAVING COUNT(1) >= 3
)