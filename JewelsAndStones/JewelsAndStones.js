/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  let count = 0;
  for (let i of stones) {
    if (jewels.includes(i)) {
      count++;
    }
  }
  return count;
};


/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  let count = 0;
  for (let i = 0; i < stones.length; i++) {
    if (jewels.indexOf(stones[i]) >= 0) {
      count++;
    }
  }
  return count;
};


/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  return [...stones].reduce((a, e) => a + jewels.includes(e), 0);
};
