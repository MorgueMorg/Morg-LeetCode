class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hashmap = {}
        for i in nums:
            if i in hashmap:
                count += hashmap[i]
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        return count