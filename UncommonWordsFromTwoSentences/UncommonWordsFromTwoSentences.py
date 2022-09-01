class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1_ = s1.split()
        lst2_ = s2.split()
        arr = []
        for i in lst1_:
            if i not in lst2_ and lst1_.count(i) == 1:
                arr.append(i)
        for j in lst2_:
            if j not in lst1_ and lst2_.count(j) == 1:
                arr.append(j)
        return arr
