class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


class Solution:
    def countSegments(self, s: str) -> int:
        return len([i for i in s.split(" ") if i!=""])


class Solution:
    def countSegments(self, s: str) -> int:
        word=0
        count=True
        for i in range(0,len(s)):
            if s[i]!=" " and count==True:
                word+=1
                count=False
            if s[i]==" ":
                count=True
        return word