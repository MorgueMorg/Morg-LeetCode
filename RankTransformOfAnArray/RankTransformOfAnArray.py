class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 1
        ranklst = list()
        sortedarr = sorted(arr)
        dic = dict()
        if len(arr) == 0:
            return []
        dic[sortedarr[0]] = 1
        for i in range(1, len(sortedarr)):
            if sortedarr[i] != sortedarr[i-1]:
                rank += 1
            dic[sortedarr[i]] = rank
        for num in arr:
            ranklst.append(dic[num])
        return ranklst