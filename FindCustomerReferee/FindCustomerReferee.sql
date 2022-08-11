/* Write your PL/SQL query statement below */

SELECT cus.name
FROM Customer cus
WHERE cus.referee_id != 2 OR cus.referee_id IS NULL;