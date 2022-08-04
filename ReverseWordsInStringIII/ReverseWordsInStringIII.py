class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return " ".join(l)


class Solution:
    def reverseWords(self, s: str) -> str:
         return ' '.join([w[::-1] for w in s.split()])


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()      
        out = []
        for word in s:                         
            i = 0
            j = (len(word) - 1)
            while (i < j):
                word = list(word)
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            a = (''.join(word))
            out.append(a)
        return(' '.join(out)) 