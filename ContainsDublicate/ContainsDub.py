class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for i in nums:
            if i not in set_:
                set_.add(i)
            else:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set(nums)
        if len(set_) == len(nums):
            return False
        return True


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupl = {}
        for i in nums:
            if i in dupl:
                return True
            else:
                dupl[i] = 1
        return False