# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Изаначальная функция
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Возвращаю новую функцию
        return self.mirror(root, root)
    # Новая функция для определения зеркальных поддеревьев, в аргументы передаю два поддерева. t -> tree
    def mirror(self, t1, t2):
        # Если оба дерева пустые, то они одинаковы, значит возвращаю true
        if not t1 and not t2:
            return True
        # Если одно из них пустое, то они разные, значит возвращаю false
        if not t1 or not t2:
            return False
        # Возвращаю сравнение двух поддеревьев, и также вызываю рекурсию, где сравниваю зеркальные значения поддеревьев
        return t1.val == t2.val and self.mirror(t1.right, t2.left) and self.mirror(t1.left, t2.right)