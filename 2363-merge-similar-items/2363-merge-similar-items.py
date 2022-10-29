class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items1:
            d[i[0]]=i[1]
        for i in items2:
            if i[0] in d.keys():
                d[i[0]]+=i[1]
            else:
                d[i[0]]=i[1]
        l=list(d.keys())
        l.sort()
        ans=[]
        for i in range(len(l)):
            if l[i] in d.keys():
                ans.append([l[i],d[l[i]]])
        return ans