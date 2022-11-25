class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        res = []
        for i in range(0, len(arr)):
            if arr[i] == target:
                res.append(i)
        return res