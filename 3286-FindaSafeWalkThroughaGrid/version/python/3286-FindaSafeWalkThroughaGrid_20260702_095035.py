# Last updated: 7/2/2026, 9:50:35 AM
1from collections import deque
2from typing import List
3
4class Solution:
5    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
6        m = len(grid)     
7        n = len(grid[0])  
8        
9        min_cost = [[float('inf')] * n for _ in range(m)]
10        
11        q = deque()
12        
13        start_cost = grid[0][0]
14        min_cost[0][0] = start_cost
15        q.append((0, 0))
16        
17        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
18        
19        while q:
20            r, c = q.popleft()
21            
22            if r == m - 1 and c == n - 1:
23                continue
24                
25            for dr, dc in directions:
26                nr, nc = r + dr, c + dc
27                
28                if 0 <= nr < m and 0 <= nc < n:
29                    next_cost = min_cost[r][c] + grid[nr][nc]
30                    
31                    if next_cost < min_cost[nr][nc]:
32                        min_cost[nr][nc] = next_cost
33                        
34                        if grid[nr][nc] == 0:
35                            q.appendleft((nr, nc))
36                        else:
37                            q.append((nr, nc))
38                            
39        return (health - min_cost[m - 1][n - 1]) >= 1