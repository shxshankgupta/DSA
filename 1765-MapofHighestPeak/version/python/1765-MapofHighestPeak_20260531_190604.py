# Last updated: 5/31/2026, 7:06:04 PM
1from collections import deque
2class Solution:
3    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
4        rows, cols = len(isWater), len(isWater[0])
5        res = [[-1] * cols for _ in range(rows)]
6        q = deque()
7        for i in range(rows):
8            for j in range(cols):
9                if isWater[i][j] == 1:
10                    res[i][j] = 0
11                    q.append((i, j))
12
13        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
14
15        while q:
16            r,c = q.popleft()
17            for dr,dc in directions:
18                nr, nc = dr + r, dc + c
19                if 0 <= nr < rows and 0 <= nc < cols and res[nr][nc] == -1:
20                    res[nr][nc] = res[r][c] + 1
21                    q.append((nr, nc))     
22        return res