/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  let l = nums.length;
  let prev_sum = (l * (l + 1)) / 2;
  let new_sum = 0;
  for (let i = 0; i < l; i++) {
    new_sum += nums[i];
  }
  return prev_sum - new_sum;
};


/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  nums.sort((a, b) => a - b);
  for (let i = 0; i <= nums.length; i++) {
    if (nums[i] != i) return i;
  }
};


/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  nums.sort((a, b) => a - b);
  if (nums[0] !== 0) return 0;
  let low = 0;
  let high = nums.length - 1;
  while (low <= high) {
    let mid = (low + high) >> 1;
    if (nums[mid] !== mid && nums[mid - 1] === mid - 1) return mid;
    else if (nums[mid] !== mid) high = mid - 1;
    else low = mid + 1;
  }
  return nums.length;
};
