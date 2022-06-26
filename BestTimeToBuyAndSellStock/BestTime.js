/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  if (prices.length === 0) return 0;
  let max_profit = 0;
  let min_price = prices[0];
  for (let i = 0; i < prices.length; i++) {
    profit = prices[i] - min_price;
    max_profit = Math.max(profit, max_profit);
    min_price = Math.min(min_price, prices[i]);
  }
  return max_profit;
};
