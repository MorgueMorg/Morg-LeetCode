class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
            else:
                maxim = max(count, maxim)
                count = 0
        return max(count, maxim)