class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        hasht = set(nums)
        print(hasht)
        for i in nums:
            if i + diff in hasht and i + 2 * diff in hasht:
                counter += 1               
        return counter