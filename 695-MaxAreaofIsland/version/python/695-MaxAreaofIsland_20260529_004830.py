# Last updated: 5/29/2026, 12:48:30 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        max_area = 0 
5
6        if not grid:
7            return 0 
8
9        def dfs(r,c):
10            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
11                return 0
12            
13            grid[r][c] = 0
14            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c -1) )
15
16        for r in range(rows):
17            for c in range(cols):
18                if grid[r][c] == 1:
19                    area = dfs(r,c)
20                    max_area = max(max_area, area)
21
22        return max_area
23
24