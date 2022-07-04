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
 * @return {boolean}
 */
var isBalanced = function (root) {
  if (!root) return true;
  let leftTree = balanced(root.left);
  let rightTree = balanced(root.right);
  if (
    Math.abs(rightTree - leftTree) <= 1 &&
    isBalanced(root.left) === true &&
    isBalanced(root.right) === true
  ) {
    return true;
  }
  return false;
};

function balanced(root) {
  if (root === null) return 0;
  return Math.max(balanced(root.left), balanced(root.right)) + 1;
}
