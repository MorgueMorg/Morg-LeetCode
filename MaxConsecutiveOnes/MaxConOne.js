/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
  let maxim = 0;
  let count = 0;
  for (let i of nums) {
    if (i == 1) {
      count++;
    } else {
      maxim = Math.max(count, maxim);
      count = 0;
    }
  }
  return Math.max(count, maxim);
};
