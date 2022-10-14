/* Write your PL/SQL query statement below */

SELECT
    SUBSTR(ac.activity_date, 0, 10) AS day,
    COUNT(DISTINCT ac.user_id) AS active_users
FROM
    activity ac
WHERE
    ac.activity_date >= TO_DATE('2019-07-27') - 29
AND
    ac.activity_date <= TO_DATE('2019-07-27')
GROUP BY
    ac.activity_date;