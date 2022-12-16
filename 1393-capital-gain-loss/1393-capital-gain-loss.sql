/* Write your PL/SQL query statement below */

select stock_name,
       sell_total-buy_total as capital_gain_loss
from 
（
select stock_name
       ,sum(case when upper(operation)='BUY' then price else 0 end) buy_total
       ,sum(case when upper(operation)='SELL' then price else 0 end)      
         sell_total
from Stocks
GROUP BY stock_name
）;