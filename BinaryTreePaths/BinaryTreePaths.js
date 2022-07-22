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
 * @return {string[]}
 */
var binaryTreePaths = function (root) {
  if (!root) return [];
  let result = [];
  function path(root, str) {
    if (!root.left && !root.right) result.push(str + root.val);
    if (root.left) path(root.left, str + root.val + "->");
    if (root.right) path(root.right, str + root.val + "->");
  }
  path(root, "");
  return result;
};
