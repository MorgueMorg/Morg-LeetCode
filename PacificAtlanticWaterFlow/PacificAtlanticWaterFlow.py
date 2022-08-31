class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, seen):
            seen.add((r, c))            
            h = heights[r][c]
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in seen and heights[nr][nc] >= h):
                    dfs(nr, nc, seen)
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        for c in range(n):
            dfs(0, c, pacific)
            
        for r in range(1, m):
            dfs(r, 0, pacific)
            
        atlantic = set()
        for c in range(n):
            dfs(m-1, c, atlantic)
            
        for r in range(0, m-1):
            dfs(r, n-1, atlantic)
            
        return atlantic & pacific