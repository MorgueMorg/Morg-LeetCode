class Solution:
    def validPath(self, n: int, E: List[List[int]], src: int, dst: int) -> bool:
        if src == dst : return True
        
        G = defaultdict(set)
        for u,v in E : G[u].add(v), G[v].add(u)
            
        dq, seen = deque([src]), set({src})
        while dq:
            v = dq.popleft()
            for u in G[v]:
                if u == dst : return True
                if u not in seen:
                    seen.add(u)
                    dq.append(u)
                
        return False