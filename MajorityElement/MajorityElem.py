class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, inter = 0, 0
        for num in nums:
            if count == 0:
                inter = num
                count += 1
            elif num == inter:
                count +=1
            else:
                count -= 1
        return inter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, inter = 0, 0
        for num in nums:
            if count == 0:
                inter = num
            count += (1 if num == inter else -1)
        return inter