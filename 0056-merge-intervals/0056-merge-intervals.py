class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = []
        intervals.sort()
        for i in intervals:
            if not arr or arr[-1][1] < i[0]:
                arr.append(i)
            else:
                arr[-1][1] = max(arr[-1][1], i[1])
        return arr