class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def traver(cand, arr, sm):
            if sm == target: res.append(arr)
            if sm >= target: return
            for i in range(len(cand)):
                traver(cand[i:], arr + [cand[i]], sm+cand[i])
        traver(candidates, [], 0)
        return res
