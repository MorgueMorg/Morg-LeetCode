class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or s is None or words is None:
            return []
        
        count = {}    # dictionary that keeps (word, count)      
        wordLength = len(words[0])   # the length of one word in words list
        res = []              # result list
        wordsLength = len(words) * wordLength   # length of the list times
        
        # fill up count dict
        for word in words:
            count[word] = count.get(word, 0) + 1
            
        # find substrings
        for left in range(len(s) - wordsLength + 1):
            # dict for keeps track of the words we find
            wordsSeen = {}
            
            for right in range(len(words)):
                wordIndex = left + right * wordLength
                tempWord = s[wordIndex : wordIndex + wordLength]
                
                if tempWord not in count:
                    break
                    
                wordsSeen[tempWord] = wordsSeen.get(tempWord, 0) + 1
                
                if wordsSeen[tempWord] > count[tempWord]:
                    break
                    
            if wordsSeen == count:
                res.append(left)
                
        return res
                