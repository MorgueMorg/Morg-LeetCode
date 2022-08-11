# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.inArr(root, arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True
    
    def inArr(self, root, arr):
        if root is None:
            return True
        self.inArr(root.left, arr)
        arr.append(root.val)
        self.inArr(root.right, arr)


        