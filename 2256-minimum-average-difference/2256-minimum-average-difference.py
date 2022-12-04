class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        cur_min = tot = sum(nums)
        n = len(nums)
        idx = 0
        cur_tot = 0
        for i, v in enumerate(nums):
            cur_tot += v
            a = cur_tot // (i + 1)
            b = 0 if i == (n - 1) else (tot - cur_tot) // (n - i - 1)
            cur = abs(a - b)
            if cur < cur_min:
                idx = i
                cur_min = cur
        return idx