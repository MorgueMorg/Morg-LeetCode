class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                t = 0
                c = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= i + dx < m and 0 <= j + dy < n:
                            t += img[i + dx][j + dy]
                            c += 1
                res[i][j] = t // c
        return res