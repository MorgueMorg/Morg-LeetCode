class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = len(nums)
        while l > 0:
            count = 0
            for i in nums:
                if i >= l:
                    count += 1
            if count == l:
                return count
            else:
                l -= 1
        return -1