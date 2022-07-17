class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        length = len(ops)
        if length == 0:
            return m*n
        result = [ops[0][0], ops[0][1]]
        for i in range(1, length):
            result[0] = min(result[0], ops[i][0])
            result[1] = min(result[1], ops[i][1])
        return result[0] * result[1]
    