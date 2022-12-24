class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        if n == 4: return 11
        if n == 5: return 24
        a,b,c = 5,11,24 #[a,b,c] => [b,c,a+c+c] => [b,c]+[2*c+a]
        for i in range(6,n+1):
            a,b,c = b,c,2*c+a
        return c % (10**9+7)