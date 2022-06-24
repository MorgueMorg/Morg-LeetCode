/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
//  */
var sortedArrayToBST = function (nums) {
  return check(nums, 0, nums.length - 1);
};

let check = function (nums, t1, t2) {
  if (t1 > t2) return null;
  let mid = Math.ceil((t1 + t2) / 2);
  let root = new TreeNode(nums[mid]);
  root.left = check(nums, t1, mid - 1);
  root.right = check(nums, mid + 1, t2);
  return root;
};
