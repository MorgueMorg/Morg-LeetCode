class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        res = [[0] * c for k in range(r)]
        for i in range(m * n):
            res[i // c][i % c] = mat[i // n][i % n]
        return res