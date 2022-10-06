class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        newLine = 1
        width = 0
        for char in s:
            charWidth = widths[ord(char) - ord('a')]
            if charWidth + width > 100:
                newLine += 1
                width = 0
            width += charWidth
        return [newLine, width]  