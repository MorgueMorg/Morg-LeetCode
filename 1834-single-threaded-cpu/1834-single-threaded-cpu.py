class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for ix in range(len(tasks)):
            tasks[ix].append(ix)
        tasks = sorted(tasks, key=lambda ix:ix[0])

        rst = []
        heap = []
        time = tasks[0][0]
        ix = 0

        while heap or ix < len(tasks):
            while ix < len(tasks) and time >= tasks[ix][0]:
                heapq.heappush(heap, [tasks[ix][1], tasks[ix][2]])
                ix += 1
            if heap:
                t, index = heapq.heappop(heap)
                time += t
                rst.append(index)
            else:
                time = tasks[ix][0]

        return rst