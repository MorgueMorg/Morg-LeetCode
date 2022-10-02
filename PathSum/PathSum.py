# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        sum_ = targetSum - root.val
        
        if sum_ == 0 and root.right == None and root.left == None:
            return True
        
        if self.hasPathSum(root.left, sum_): return True
        if self.hasPathSum(root.right, sum_): return True
        
        return False