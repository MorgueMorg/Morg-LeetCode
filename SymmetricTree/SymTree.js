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
  // Новая функция для определения зеркальных поддеревьев, в аргументы передаю два поддерева. t -> tree
  mirror = (t1, t2) => {
    if (!t1 && !t2) {
      // Если оба дерева пустые, то они одинаковы, значит возвращаю true
      return true;
    } else if (!t1 || !t2) {
      // Если одно из них пустое, то они разные, значит возвращаю false
      return false;
    } else {
      return (
        // Возвращаю сравнение двух поддеревьев, и также вызываю рекурсию, где сравниваю зеркальные значения поддеревьев
        t1.val == t2.val &&
        mirror(t1.right, t2.left) &&
        mirror(t1.left, t2.right)
      );
    }
  };
  //   Возвращаю новую функцию
  return mirror(root, root);
};
