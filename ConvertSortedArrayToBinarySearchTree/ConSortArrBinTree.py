# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # t1 и t2 это два поддерева нашего дерева (t1 левая сторона, t2 правая)
        def check(t1, t2):
            # Левая сторона всегда меньше чем правая, потому что у нас сбаланc. двоичное дерево
            # Фукнция рекурсивная, поэтому нужно обработать базовый случай
            if t1 > t2:
                return None
            # mid - это ноль в массиве(дереве), то есть корневой узел
            mid = (t1 + t2) // 2
            # TreeNode это класс сверху, беру середину по индексу из массива (корневой узел)
            root = TreeNode(nums[mid])
            # Тут рекурсия
            # Так как это левое дерево, первый указатель остается
            root.left = check(t1, mid - 1)
            # Тут тоже самое, но к правому +1, потому что левое поддерево должно быть меньше
            root.right = check(mid + 1, t2)
            # Возвращаю корень
            return root
        # Возвращаю ф-ию, где 0 это левое поддерево, а второе это длина массива - 1
        return check(0, len(nums) - 1)