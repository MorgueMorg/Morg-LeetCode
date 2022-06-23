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
var isSymmetric = function (root) {
  mirror = (t1, t2) => {
    if (!t1 && !t2) {
      return true;
    } else if (!t1 || !t2) {
      return false;
    } else {
      return (
        t1.val == t2.val &&
        mirror(t1.right, t2.left) &&
        mirror(t1.left, t2.right)
      );
    }
  };
  return mirror(root, root);
};
