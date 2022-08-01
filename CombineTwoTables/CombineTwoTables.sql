/* Write your PL/SQL query statement below */
SELECT p.firstName, p.lastName, city, state
FROM Person p
LEFT JOIN Address ad on ad.PersonId = p.PersonId