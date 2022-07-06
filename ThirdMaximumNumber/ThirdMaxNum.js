/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function (nums) {
  let arr = new Set(nums);
  if (arr.size < 3) return Math.max(...arr);
  arr.delete(Math.max(...arr));
  arr.delete(Math.max(...arr));
  return Math.max(...arr);
};


var thirdMax = function (nums) {
  nums = [...new Set(nums)].sort((a, b) => b - a);
  return nums.length >= 3 ? nums[2] : nums[0];
};
