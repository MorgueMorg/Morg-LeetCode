class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance, visited = tuple(entrance), set()
        n, m = len(maze), len(maze[0])
        for i in range(n):
            if maze[i][0] == '.':
                visited.add((i, 0))
            if maze[i][m-1] == '.':
                visited.add((i, m-1))
        for j in range(m):
            if maze[0][j] == '.':
                visited.add((0, j))
            if maze[n-1][j] == '.':
                visited.add((n-1, j))

        if entrance in visited: 
            visited.remove(entrance)

        q = deque(visited)

        res = 0
        ngs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r, c) == entrance:
                    return res
                for u, v in ngs:
                    row, col = r + u, c + v
                    if (row not in range(n) or 
                        col not in range(m) or
                        maze[row][col] == '+' or
                        (row, col) in visited):
                        continue
                    visited.add((row, col))
                    q.append((row, col))
            res += 1
        return -1