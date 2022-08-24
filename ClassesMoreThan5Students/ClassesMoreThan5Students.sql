/* Write your PL/SQL query statement below */

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5