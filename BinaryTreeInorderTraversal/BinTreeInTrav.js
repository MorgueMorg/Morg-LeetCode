/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
  let stack = [];
  let now = root;
  let res = [];

  while (now || stack.length) {
    while (now) {
      stack.push(now);
      now = now.left;
    }
    now = stack.pop();
    res.push(now.val);
    now = now.right;
  }

  return res;
};
