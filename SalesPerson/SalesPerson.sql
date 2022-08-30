/* Write your PL/SQL query statement below */

Select s.name 
FROM SalesPerson s 
WHERE s.sales_id not in (
    SELECT o.sales_id 
    FROM Orders o 
    INNER JOIN Company c
    ON o.com_id = c.com_id
    where c.name = 'RED'
);