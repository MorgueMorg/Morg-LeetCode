/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    let j = nums[i];
    if (obj[j] !== undefined && i - obj[j] <= k) {
      return true;
    }
    obj[j] = i;
  }
  return false;
};


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (i - map.get(nums[i]) <= k) {
      return true;
    }
    map.set(nums[i], i);
  }
  return false;
};


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i])) {
      const j = map.get(nums[i]);

      if (Math.abs(i - j) <= k) {
        return true;
      }
    }

    map.set(nums[i], i);
  }

  return false;
};
