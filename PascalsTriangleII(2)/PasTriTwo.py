class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]*(rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j-1]
        return result


# ! Solution 2
class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row