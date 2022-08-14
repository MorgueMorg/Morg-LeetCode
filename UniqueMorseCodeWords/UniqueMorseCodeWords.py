class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morze = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            val = ""
            for i in word:
                val += morze[ord(i)- ord("a")]
            res.add(val)
        return len(res)