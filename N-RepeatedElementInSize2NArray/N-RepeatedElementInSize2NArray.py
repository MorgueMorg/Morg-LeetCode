class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                return i


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        res=0
        c=0
        for i in nums:
            d[i]=1+d.get(i,0)
            res=max(d[i],res)
            if res==d[i]:
                c=i
        return c