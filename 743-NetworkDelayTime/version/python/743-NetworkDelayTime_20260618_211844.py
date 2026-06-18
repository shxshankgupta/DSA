# Last updated: 6/18/2026, 9:18:44 PM
1import heapq
2from collections import defaultdict
3class Solution:
4    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
5        adj = defaultdict(list)
6        for u, v, w in times:
7            adj[u].append((v, w))
8
9        result = [float('inf')] * (n + 1)
10        result[k] = 0
11
12        pq =[]
13        heapq.heappush(pq, (0, k))
14
15        while pq:
16            d, u = heapq.heappop(pq)
17
18            if d > result[u]:
19                continue
20
21            for v, w in adj[u]:
22                if d + w < result[v]:
23                    result[v] = d + w
24                    heapq.heappush(pq, (result[v], v))
25
26        max_time = 0 
27        
28        for i in range(1, n + 1):
29            if result[i] == float('inf'):
30                return -1
31            max_time = max(max_time, result[i])
32
33        return max_time
34
35