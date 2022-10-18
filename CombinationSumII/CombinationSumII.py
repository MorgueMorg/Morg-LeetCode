class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
        
    def dfs(self, nums, target, idx, path, res):
        if target <= 0:
            if target == 0:
                res.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)