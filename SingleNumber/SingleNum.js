/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }
  let result = 0;
  nums.forEach((element) => {
    // ^ -> Проводит побитовую операцию xor (исключающее или) на двух значениях. x = x ^ i
    result = result ^ element;
  });
  return result;
};


// ! Solution 2
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  let i = 0;
  nums.forEach((e) => {
    if (nums.filter((n) => n === e).length === 1) i = e;
  });
  return i;
};
