class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            for n in nums:
                if n == i:
                    dp[i] += 1
                if n < i:
                    dp[i] += dp[i - n]
        return dp[-1]