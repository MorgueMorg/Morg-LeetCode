class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for q in queries:
            s=0 #sum of subsequence
            l=0 #length of subsequence
            for i in nums:
                if s+i<=q: #check before adding the element.
                    s=s+i
                    l=l+1
                else:
                    break
            ans.append(l)
        return ans