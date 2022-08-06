/* Write your PL/SQL query statement below */

SELECT ac.player_id, TO_CHAR(MIN(TO_DATE(event_date, 'yyyy-mm-dd'))) AS first_login
FROM Activity ac
GROUP BY player_id