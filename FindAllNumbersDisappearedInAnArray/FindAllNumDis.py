class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        num_set = set(range(1, length + 1))
        for i in nums:
            if i in num_set:
                num_set.remove(i)
        return list(num_set)    