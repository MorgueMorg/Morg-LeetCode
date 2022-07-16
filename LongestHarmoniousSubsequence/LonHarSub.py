class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else: mp[i]+=1
        ln=0;
        for i in mp:
            if mp.get(i+1):
                ln=max(ln,mp[i]+mp[i+1])
        return ln 