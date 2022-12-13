class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l=len(matrix)
        # Iterating from 2nd row of matrix and creating matrix of minimum sum upto that point.
        for i in range(1,l):
            # For every cell, adding the minimum of three values above it.
            matrix[i][0]+=min(matrix[i-1][0:2])
            for j in range(1,l):
                matrix[i][j]+=min(matrix[i-1][j-1:j+2])
        # Returning minimum of last step.
        return min(matrix[l-1])