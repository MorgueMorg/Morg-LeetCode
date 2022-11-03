class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        combos = {}
        count = 0
        
        for word in words:
            if word[::-1] in combos and combos[word[::-1]] >= 0:
                count += 4
                combos[word[::-1]] -= 1
            else:
                if word in combos:
                    combos[word] += 1
                else:
                    combos[word] = 0      
                    
        for word in words:
            if word == word[::-1]:
                if combos[word] >= 0:
                    return count + 2
                
        return count
    