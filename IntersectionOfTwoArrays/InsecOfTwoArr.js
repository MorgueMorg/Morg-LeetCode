/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  nums1 = new Set(nums1);
  return nums2.filter((num) => nums1.delete(num));
};


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  let arr = [];
  nums1.forEach((num) => {
    if (nums2.indexOf(num) != -1) {
      arr.push(num);
    }
  });
  let res = [...new Set(arr)];
  return res;
};


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  let hash = {};
  let arr = [];
  for (let num of nums1) {
    hash[num] = true;
  }
  for (let i = 0; i < nums2.length; i++) {
    if (hash[nums2[i]]) {
      arr.push(nums2[i]);
    }
  }
  return [...new Set(arr)];
};


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  nums1 = nums1.sort((a, b) => a - b);
  nums2 = nums2.sort((a, b) => a - b);
  let arr = [];
  for (let i of nums1) {
    let left = 0;
    let right = nums2.length - 1;
    while (left <= right) {
      let mid = Math.ceil((left + right) / 2);
      if (nums2[mid] === i) {
        if (!arr.includes(i)) {
          arr.push(i);
        }
        break;
      } else if (nums2[mid] > i) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  }
  return arr;
};
