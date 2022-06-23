/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

 // ! Использовал рекурсию, проверил каждое поддерево(глубокий поиск)
 // ! Параметры val, left и right прописаны сверху в конструкторе this, обозначают стороны дерева

var isSameTree = function (p, q) {
  if (!p && !q) {
    // если оба дерева пусты(false), то значит одинаковы и возвращаю true
    return true;
  } else if (!p || !q || p.val != q.val) {
    // Если их значение не равны друг другу или одно пустое, возвращаю false
    return false;
  } else {
    // Либо же возвращаю рекурсию со сторонами деревьев
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  }
};
