# Last updated: 6/1/2026, 2:32:36 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        if not heights or not heights[0]:
4            return []
5
6        rows, cols = len(heights), len(heights[0])
7        pacificReach = [[False] * cols for _ in range(rows)]
8        atlanticReach = [[False] * cols for _ in range(rows)]
9
10        def dfs(r, c, prev_height, visited):
11            if (r < 0 or r >= rows or c < 0 or c >= cols or 
12                visited[r][c] or heights[r][c] < prev_height):
13                return
14            
15            visited[r][c] = True
16            
17            dfs(r + 1, c, heights[r][c], visited)
18            dfs(r - 1, c, heights[r][c], visited)
19            dfs(r, c + 1, heights[r][c], visited)
20            dfs(r, c - 1, heights[r][c], visited)
21            
22        for r in range(rows):
23            dfs(r, 0, float('-inf'), pacificReach)
24            dfs(r, cols - 1, float('-inf'), atlanticReach)
25        
26        for c in range(cols):
27            dfs(0, c, float('-inf'), pacificReach)
28            dfs(rows - 1, c, float('-inf'), atlanticReach)
29
30        res = []
31        for m in range(rows):
32            for n in range(cols):
33                if pacificReach[m][n] == True and atlanticReach[m][n] == True:
34                    res.append([m, n])
35        
36        return res