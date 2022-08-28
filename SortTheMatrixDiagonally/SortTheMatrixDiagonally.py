class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        mat_cols = len(mat[0])
        mat_rows = len(mat)
        unsorted = True
        
        while unsorted:
            unsorted = False
            for col in range(mat_cols - 1):
                for row in range(mat_rows - 1):
                    if mat[row][col] > mat[row + 1][col + 1]:
                        unsorted = True
                        mat[row][col], mat[row + 1][col + 1] = mat[row + 1][col + 1], mat[row][col]
            
        return mat