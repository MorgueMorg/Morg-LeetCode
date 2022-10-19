# TODO import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dc = {}
        res = []
        heap = []
        for i in words:
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1
        for i in dc:
            heapq.heappush(heap,(-1 * dc[i],i))
        for i in range(k):
            if heapq:
                x = heapq.heappop(heap)
                res.append(x[1])
        return res