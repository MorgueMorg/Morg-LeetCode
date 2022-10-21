class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        
        if nums.count(target) == 0:
            return [-1,-1]
        
        res.append(nums.index(target))
        for x in range(len(nums) -1 , -1 , -1 ):
            if nums[x] == target:
                res.append(x)
                break
        
        return res