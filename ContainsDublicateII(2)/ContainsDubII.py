class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        obj = {}
        for i, j in enumerate(nums):
            if j not in obj:
                obj[j] = i
            else:
                if i - obj[j] <= k:
                    return True
                obj[j] = i
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        obj = {}
        for i, j in enumerate(nums):
            if j in obj and i - obj[j] <= k:
                return True
            else:
                obj[j] = i
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i

        return False