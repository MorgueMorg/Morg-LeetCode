class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        bucket = [0 for _ in range(10001)]
        ans = sum(piles)
        for i in piles:
            bucket[i] += 1
        for i in range(10000, -1, -1):
            while bucket[i] > 0 and k > 0:
                k -= 1  
                bucket[i] -= 1
                temp = i // 2
                ans -= temp
                bucket[i-temp] += 1
            if k == 0: 
                return ans