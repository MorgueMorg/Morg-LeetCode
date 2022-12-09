# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, high, low):
            if node:
                high = max(node.val, high)
                low = min(node.val, low)

                dfs(node.left, high, low)
                dfs(node.right, high, low)

                diff = max(abs(node.val - high), abs(node.val - low))
                self.ans = max(self.ans, diff)
        
        dfs(root, float('-inf'), float('inf'))
        return self.ans