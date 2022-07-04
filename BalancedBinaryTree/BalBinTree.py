# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            if root == None:
                return True
            leftTree = balanced(root.left)
            if leftTree == - 1:
                return -1
            rightTree = balanced(root.right)
            if rightTree == - 1:
                return -1
            if abs(leftTree - rightTree) > 1:
                return -1
            return max(leftTree, rightTree) + 1
        return balanced(root) != -1