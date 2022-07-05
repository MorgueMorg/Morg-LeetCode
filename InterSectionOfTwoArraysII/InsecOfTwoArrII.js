/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  let arr = [];
  nums1.map((num1, i) => {
    if (nums2.includes(num1)) {
      arr.push(num1);
      nums2.splice(nums2.indexOf(num1), 1);
    }
  });
  return arr;
};


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersect = function (nums1, nums2) {
    nums1.sort((a, b) => a - b)
    nums2.sort((a, b) => a - b)
    let arr = []
    let i = 0, j = 0
    while(i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) i++
        else if (nums2[j] < nums1[i]) j++
        else {
            arr.push(nums1[i])
            i++
            j++
        }
    }
    return arr
};
