/**
 * @param {number[]} nums
 */
var NumArray = function (nums) {
  this.arr = [];
  this.arr[0] = 0;
  for (let num = 1; num <= nums.length; num++) {
    this.arr[num] = this.arr[num - 1] + nums[num - 1];
  }
};

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function (left, right) {
  return this.arr[right + 1] - this.arr[left];
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */


