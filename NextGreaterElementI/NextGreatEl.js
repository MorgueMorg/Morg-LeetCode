/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
  return nums1.map((n) => {
    let next = nums2.indexOf(n) + 1;
    while (next < nums2.length && nums2[next] < n) {
      next++;
    }
    return next >= nums2.length ? -1 : nums2[next];
  });
};
