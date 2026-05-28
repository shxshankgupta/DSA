# Last updated: 5/29/2026, 12:26:31 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        islands = 0
5        if not grid :
6            return 0
7
8        def dfs(r,c):
9            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
10                return
11            
12            grid[r][c] = '0'
13
14            dfs(r + 1, c)
15            dfs(r - 1, c)
16            dfs(r, c + 1)
17            dfs(r, c -1)
18
19        
20        for r in range(rows):
21            for c in range(cols):
22                if grid[r][c] == '1':
23                    islands += 1
24                    dfs(r,c)
25        
26        return islands
27
28        