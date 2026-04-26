# Last updated: 4/26/2026, 9:12:16 AM
1class Solution:
2    def containsCycle(self, grid: List[List[str]]) -> bool:
3        ROWS, COLS = len(grid), len(grid[0])
4        visited = set()
5
6        def dfs(r, c, pr, pc, char):
7            visited.add((r, c))
8            
9            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
10                nr, nc = r + dr, c + dc
11                
12                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == char:
13                    if (nr, nc) in visited and (nr, nc) != (pr, pc):
14                        return True
15                    if (nr, nc) not in visited:
16                        if dfs(nr, nc, r, c, char):
17                            return True
18            return False
19
20        for r in range(ROWS):
21            for c in range(COLS):
22                if (r, c) not in visited:
23                    if dfs(r, c, -1, -1, grid[r][c]):
24                        return True
25        
26        return False