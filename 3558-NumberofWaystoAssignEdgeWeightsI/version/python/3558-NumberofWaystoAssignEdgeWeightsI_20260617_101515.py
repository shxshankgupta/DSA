# Last updated: 6/17/2026, 10:15:15 AM
1from collections import defaultdict
2import sys
3
4sys.setrecursionlimit(200000)
5
6class Solution:
7    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
8        MOD = 10**9 + 7
9        
10        graph = defaultdict(list)
11        for u, v in edges:
12            graph[u].append(v)
13            graph[v].append(u)
14            
15        max_depth = 0
16        
17        def dfs(node, parent, depth):
18            nonlocal max_depth
19            max_depth = max(max_depth, depth)
20            
21            for neighbor in graph[node]:
22                if neighbor != parent:
23                    dfs(neighbor, node, depth + 1)
24                    
25        dfs(1, -1, 0)
26        
27        if max_depth == 0:
28            return 0
29            
30        return pow(2, max_depth - 1, MOD)