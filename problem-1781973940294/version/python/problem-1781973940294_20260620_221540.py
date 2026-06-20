# Last updated: 6/20/2026, 10:15:40 PM
1import sys
2from typing import List
3
4sys.setrecursionlimit(200000)
5
6class Solution:
7    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
8        torqavemi = n
9        
10        adj = [[] for _ in range(n)]
11        for u, v in edges:
12            adj[u].append(v)
13            
14        def dfs(node):
15            if not adj[node]:
16                return baseTime[node]
17            
18            children_times = [dfs(child) for child in adj[node]]
19            
20            earliest = min(children_times)
21            latest = max(children_times)
22            
23            own_duration = (latest - earliest) + baseTime[node]
24            
25            return latest + own_duration
26
27        return dfs(0)