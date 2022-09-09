class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        arr = []
        for i in range(rows):
            for j in range(cols):
                arr.append([i, j])
        arr = sorted(arr, key=lambda x: abs(x[0]-rCenter) + abs(x[1]-cCenter))
        return arr