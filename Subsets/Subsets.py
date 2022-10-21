class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        for i in nums:
            for j in range(len(arr)):
                x = arr[j][:]
                x.append(i)
                arr.append(x)
        return arr