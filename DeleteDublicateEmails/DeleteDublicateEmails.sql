/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 */

DELETE 
FROM Person
WHERE id NOT IN (
    SELECT min(id)
    FROM Person
    GROUP BY email
)