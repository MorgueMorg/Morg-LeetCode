# Not sorting
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            arr.append(count)
        return arr
                

# Sorting
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n1 = sorted(nums)
        ans  = []
        mp = {}
        for i,x in enumerate(n1):
            if x in mp:
                mp[x] = min(mp[x], i)
            else:
                mp[x]=i 
        for i in nums:    
            ans.append(mp.get(i))
        return ans