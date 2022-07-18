/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function (nums) {
  let map = new Map();
  let len = nums.length;
  let sum = (len * (len + 1)) / 2;
  let s = 0,
    a = 0;
  for (let i = 0; i < len; i++) {
    if (map.has(nums[i])) a = nums[i];
    else {
      map.set(nums[i], true);
      s += nums[i];
    }
  }
  return [a, sum - s];
};
