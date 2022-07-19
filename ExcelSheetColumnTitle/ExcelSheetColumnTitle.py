class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber > 0:
            arr.append(chr((columnNumber - 1) % 26 + ord("A")))
            columnNumber = (columnNumber - 1) // 26
        arr.reverse()
        return "".join(arr)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "" 
        while columnNumber > 0:
            columnNumber,rem = divmod(columnNumber-1,26)
            s += chr(65+rem)
        return s[::-1]