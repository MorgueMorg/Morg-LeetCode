/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function (nums) {
  let count = 1,
    long = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < nums[i + 1]) count++;
    else count = 1;
    long = Math.max(count, long);
  }
  return long;
};
