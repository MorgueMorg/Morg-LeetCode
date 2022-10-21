# ! Iterative
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        for i in nums:
            for j in range(len(arr)):
                x = arr[j][:]
                x.append(i)
                arr.append(x)
        return arr


# ! Recursion
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        def powerSet(nums, i, subSet): 
            if i==n:
                result.append(subSet) 
                return 
            powerSet(nums, i+1, subSet) 
            powerSet(nums, i+1, subSet + [nums[i]]) 
        powerSet(nums, 0, [])
        return result 