/* Write your PL/SQL query statement below */

SELECT 
    TO_CHAR(event_day, 'YYYY-MM-DD') AS day, 
    emp_id, 
    SUM(out_time - in_time) total_time
FROM Employees
GROUP BY event_day, emp_id