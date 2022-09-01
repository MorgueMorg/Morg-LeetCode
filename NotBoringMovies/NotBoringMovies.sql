/* Write your PL/SQL query statement below */

SELECT * 
FROM Cinema
-- MOD в oracle возвращает остаток от деления
WHERE mod(id,2) != 0
AND description != 'boring'
ORDER BY rating desc;