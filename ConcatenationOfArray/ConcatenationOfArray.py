class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        while len(res) != len(nums) * 2:
            res.extend(nums)
        return res