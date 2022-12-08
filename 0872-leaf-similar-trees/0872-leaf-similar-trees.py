# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node,leaf):
            
            if node:
                if not node.left and not node.right:
                    leaf.append(node.val)
                helper(node.left,leaf)
                helper(node.right,leaf)
            return leaf
        
        return helper(root1,[]) == helper(root2,[])