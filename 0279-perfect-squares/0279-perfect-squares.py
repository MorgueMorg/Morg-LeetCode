class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x**2 for x in range(0, n) if x**2<=n]
        sqs = [n]*(n+1)
        sqs[0] = 0 
        for i in range(1, n+1):
            for sq in squares: 
                if i - sq < 0: 
                    break
                if 1 + sqs[i-sq] < sqs[i]:
                    sqs[i] = 1 + sqs[i-sq]    
        return sqs[n]