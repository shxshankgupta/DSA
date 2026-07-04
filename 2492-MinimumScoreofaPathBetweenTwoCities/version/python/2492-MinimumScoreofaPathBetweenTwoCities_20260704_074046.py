# Last updated: 7/4/2026, 7:40:46 AM
1from collections import deque
2class Solution:
3    def minScore(self, n: int, roads: List[List[int]]) -> int:
4        adj = {}
5        for road in roads:
6            u, v, w = road[0], road[1], road[2]
7
8            if u not in adj:
9                adj[u] = []
10            adj[u].append((v, w))
11
12            if v not in adj:
13                adj[v] = []
14            adj[v].append((u, w))
15
16        q = deque([1])
17        visited = {1}
18        ans = float('inf')
19
20        while q:
21            u = q.popleft()
22
23            for v, w in adj[u]:
24                ans = min(ans, w)
25
26                if v not in visited :
27                    visited.add(v)
28                    q.append(v)
29
30        return ans
31
32
33        
34