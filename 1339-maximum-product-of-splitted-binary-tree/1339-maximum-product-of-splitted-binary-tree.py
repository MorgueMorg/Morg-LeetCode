# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        if root is None: return 0
        arr = []
        tot = self.dfs(root, arr)
        res = 0
        for x in arr:
            res = max(res, x * (tot - x))
        return res % MOD
    
    def dfs(self, root, arr):
        if not root:
            return 0
        L = self.dfs(root.left, arr)
        R = self.dfs(root.right, arr)
        now = L + R + root.val
        arr.append(now)
        return now
