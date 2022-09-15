class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = list()
        for i in range(len(mat)):
            s = sum(mat[i])
            soldiers.append((s,i))    
        soldiers = sorted(soldiers, key= lambda x: x[0])
        return [s[1] for s in soldiers[:k]]