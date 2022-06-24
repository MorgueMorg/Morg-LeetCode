# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def check(t1, t2):
            if t1 > t2:
                return None
            mid = (t1 + t2) // 2
            root = TreeNode(nums[mid])
            root.left = check(t1, mid - 1)
            root.right = check(mid + 1, t2)
            return root
        return check(0, len(nums) - 1)