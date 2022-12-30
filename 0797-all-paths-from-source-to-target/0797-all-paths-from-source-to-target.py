class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        stack = [(0,)]
        while stack:
            cur_path = stack.pop()
            cur = cur_path[-1]
            if cur == len(graph) - 1:
                res.append(cur_path)
            for nei in graph[cur]:
                stack.append(cur_path + (nei,))
        return res