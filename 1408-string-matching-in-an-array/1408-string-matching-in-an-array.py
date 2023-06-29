class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in range(len(words)):
            for i in range(word, len(words)):
                if words[i] == words[word]:
                    continue
                else:
                    if words[word] in words[i]:
                        res.append(words[word])
                    elif words[i] in words[word]:
                        res.append(words[i])
                    else: 
                        continue
        return set(res)