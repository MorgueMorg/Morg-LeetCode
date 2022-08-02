class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def helper(matrix, val):
            order = 0
            for row in matrix:
                for col in row:
                    if col <= val: order += 1
            return order
            
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            order = helper(matrix, mid)
            if order >= k:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in matrix:
            res += i
        return sorted(res)[k-1]