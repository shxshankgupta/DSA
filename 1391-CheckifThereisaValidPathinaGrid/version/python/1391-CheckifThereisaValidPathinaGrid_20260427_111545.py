# Last updated: 4/27/2026, 11:15:45 AM
1class Solution:
2    def hasValidPath(self, grid: List[List[int]]) -> bool:
3        m, n = len(grid), len(grid[0])
4        directions = {
5            1: [(0, -1), (0, 1)],
6            2: [(-1, 0), (1, 0)],
7            3: [(0, -1), (1, 0)],
8            4: [(0, 1), (1, 0)],
9            5: [(0, -1), (-1, 0)],
10            6: [(0, 1), (-1, 0)]
11        }
12        
13        visited = set([(0, 0)])
14        queue = collections.deque([(0, 0)])
15        
16        while queue:
17            r, c = queue.popleft()
18            if r == m - 1 and c == n - 1:
19                return True
20                
21            for dr, dc in directions[grid[r][c]]:
22                nr, nc = r + dr, c + dc
23                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
24                    for back_dr, back_dc in directions[grid[nr][nc]]:
25                        if nr + back_dr == r and nc + back_dc == c:
26                            visited.add((nr, nc))
27                            queue.append((nr, nc))
28                            break
29                            
30        return False