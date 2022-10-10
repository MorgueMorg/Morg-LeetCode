/* Write your PL/SQL query statement below */

SELECT product_id, product_name
FROM PRODUCT
WHERE product_id IN (
    SELECT product_id 
    FROM SALES
    MINUS
    SELECT product_id 
    FROM SALES
    WHERE sale_date NOT BETWEEN TO_DATE('2019-01-01') 
    AND TO_DATE('2019-03-31')
)