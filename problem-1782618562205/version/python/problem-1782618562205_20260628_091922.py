# Last updated: 6/28/2026, 9:19:22 AM
1import heapq
2from typing import List
3
4class Solution:
5    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
6        midway = (n, edges, power, cost, source, target)
7        
8        adj = [[] for _ in range(n)]
9        for u, v, t in edges:
10            adj[u].append((v, t))
11            
12        min_time = [[float('inf')] * (power + 1) for _ in range(n)]
13        min_time[source][power] = 0
14        
15        pq = [(0, -power, source)]
16        
17        while pq:
18            curr_time, neg_power, u = heapq.heappop(pq)
19            curr_power = -neg_power
20            
21            if u == target:
22                return [curr_time, curr_power]
23                
24            if curr_time > min_time[u][curr_power]:
25                continue
26                
27            if curr_power >= cost[u]:
28                next_power = curr_power - cost[u]
29                
30                for v, t in adj[u]:
31                    next_time = curr_time + t
32                    
33                    if next_time < min_time[v][next_power]:
34                        min_time[v][next_power] = next_time
35                        heapq.heappush(pq, (next_time, -next_power, v))
36                        
37        return [-1, -1]