/* Write your PL/SQL query statement below */

SELECT cu.name AS Customers
FROM Customers cu
LEFT JOIN Orders ord on cu.id = ord.customerId
WHERE ord.customerId IS NULL