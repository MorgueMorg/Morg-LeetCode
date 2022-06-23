# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ! Использовал рекурсию, проверил каждое поддерево(глубокий поиск)
# ! Параметры val, left и right прописаны сверху в конструкторе init, обозначают стороны дерева
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if если оба дерева пусты(false), то значит одинаковы и возвращаю true
        if not p and not q: return True
        # Если их значение не равны друг другу или одно пустое, возвращаю false
        if not p or not q or p.val != q.val: return False
        # Либо же возвращаю рекурсию со сторонами деревьев, не забываю self ввиду ооп
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)