class Solution:
    def longestPalindrome(self, s: str) -> str:
        size=len(s)
        while(size>0):
            for i in range(len(s)-size+1):
                x=s[i:i+size]
                if x==x[::-1]:
                    return x
            size-=1