class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ans = 0
        subtree = {}
        
        def dfs(node, prev, depth):
            total = 1
            nonlocal ans
            ans+=depth
            for child in g[node]:
                if child == prev:
                    continue
                total+=dfs(child, node, depth + 1)
            subtree[node] = total
            return total
        
        dfs(0, None, 0)
        res = [0] * n
        res[0] = ans
        
        def dfs2(node, prev):
            for child in g[node]:
                if child == prev:
                    continue
                res[child] = res[node] - subtree[child] + (n-subtree[child])
                dfs2(child, node)
                
        dfs2(0, None)
        return res