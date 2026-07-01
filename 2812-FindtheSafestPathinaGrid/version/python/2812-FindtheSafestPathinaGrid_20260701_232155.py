# Last updated: 7/1/2026, 11:21:55 PM
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
11        dist = [[float('inf')] * n for _ in range(n)]
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
26                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
27                    dist[nr][nc] = dist[r][c] + 1
28                    q.append((nr, nc))
29        
30        def canReach(safeness: int) -> bool:
31            if dist[0][0] < safeness or dist[n-1][n-1] < safeness:
32                return False
33                
34            visited = [[False] * n for _ in range(n)]
35            check_q = deque([(0, 0)])
36            visited[0][0] = True
37            
38            while check_q:
39                r, c = check_q.popleft()
40                if r == n - 1 and c == n - 1:
41                    return True
42                    
43                for dr, dc in directions:
44                    nr, nc = r + dr, c + dc
45                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
46                        if dist[nr][nc] >= safeness:
47                            visited[nr][nc] = True
48                            check_q.append((nr, nc))
49            return False
50
51        low = 0
52        high = min(dist[0][0], dist[n-1][n-1])
53        ans = 0
54        
55        while low <= high:
56            mid = low + (high - low) // 2
57            
58            if canReach(mid):
59                ans = mid       
60                low = mid + 1
61            else:
62                high = mid - 1  
63                
64        return ans