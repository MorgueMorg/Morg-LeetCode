/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
  let index = 0;
  let ranges = [];
  for (let num = 0; num < nums.length; num++) {
    if (num + 1 < nums.length && nums[num] + 1 == nums[num + 1]) {
      continue;
    } else if (index == num) {
      ranges.push(`${nums[index]}`);
    } else {
      ranges.push(`${nums[index]}->${nums[num]}`);
    }
    index = num + 1;
  }
  return ranges;
};
