# Last updated: 7/2/2026, 8:37:38 AM
1from collections import deque
2
3class Solution:
4    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
5        n = len(grid)
6        
7
8        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
9            return 0
10        
11        dist = [[-1] * n for _ in range(n)]
12        q = deque()
13
14        for i in range(n):
15            for j in range(n):
16                if grid[i][j] == 1:
17                    q.append((i, j))
18                    dist[i][j] = 0
19                    
20        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
21        
22        while q:
23            r, c = q.popleft()
24            for dr, dc in directions:
25                nr, nc = r + dr, c + dc
26                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
27                    dist[nr][nc] = dist[r][c] + 1
28                    q.append((nr, nc))
29        
30        def canReach(safeness: int) -> bool:
31            
32                
33            visited = [[False] * n for _ in range(n)]
34            check_q = deque([(0, 0)])
35            visited[0][0] = True
36            
37            while check_q:
38                r, c = check_q.popleft()
39                if r == n - 1 and c == n - 1:
40                    return True
41                    
42                for dr, dc in directions:
43                    nr, nc = r + dr, c + dc
44                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
45                        if dist[nr][nc] >= safeness:
46                            visited[nr][nc] = True
47                            check_q.append((nr, nc))
48            return False
49
50        low = 0
51        high = min(dist[0][0], dist[n-1][n-1])
52        ans = 0
53        
54        while low <= high:
55            mid = low + (high - low) // 2
56            
57            if canReach(mid):
58                ans = mid       
59                low = mid + 1
60            else:
61                high = mid - 1  
62                
63        return ans