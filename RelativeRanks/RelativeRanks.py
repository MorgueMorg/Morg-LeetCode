class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse=True)
        l = len(arr)
        dict_ = {}
        dict_[arr[0]] = "Gold Medal"
        if l > 1:
            dict_[arr[1]] = "Silver Medal"
        if l > 2:
            dict_[arr[2]] = "Bronze Medal"
        for i in range(3, len(arr)):
            dict_[arr[i]] = str(i + 1)
        answer = [dict_[k] for k in score]
        return answer
            
            