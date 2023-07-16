class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        count = {}
        pos = -1
        for index, letter in enumerate(s):
            if letter in count and count[letter] > pos:
                pos = count[letter]
            count[letter] = index 
            output = max(output,index-pos)
        return output