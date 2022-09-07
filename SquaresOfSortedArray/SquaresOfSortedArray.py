class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            sq = nums[i] * nums[i]
            arr.append(sq)
            arr.sort()
        return arr