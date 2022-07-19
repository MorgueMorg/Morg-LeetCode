class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hasht = {}
        for i, n in enumerate(nums):
            if n in hasht:
                hasht[n].append(i)
            else:
                hasht[n] = [i]
        maxim = max([len(i) for i in hasht.values()])
        return min([i[-1] - i[0] for i in hasht.values() if len(i) == maxim]) + 1