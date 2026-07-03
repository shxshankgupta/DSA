# Last updated: 7/3/2026, 11:20:57 PM
1from typing import List
2import heapq
3
4class Solution:
5    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
6        n = len(online)
7        adj = {}
8
9        l = float('inf')
10        r = 0
11
12        for edge in edges:
13            u, v, cost = edge[0], edge[1], edge[2]
14
15            if not online[u] or not online[v]:
16                continue
17
18            if u not in adj:
19                adj[u] = []
20            adj[u].append((v, cost))
21            
22            l = min(l, cost)
23            r = max(r, cost)
24
25        def check(mid: int) -> bool:
26            result = [float('inf')] * n
27            result[0] = 0
28            min_heap = [(0, 0)]  
29            
30            while min_heap:
31                d, u = heapq.heappop(min_heap)
32                
33                if d > k:
34                    return False
35                if result[u] < d:
36                    continue
37                if u == n - 1:
38                    return True
39                    
40                if u in adj:
41                    for v, cost in adj[u]:
42                        if cost < mid:
43                            continue
44                        if v != n - 1 and not online[v]:
45                            continue
46                            
47                        if d + cost < result[v]:
48                            result[v] = d + cost
49                            heapq.heappush(min_heap, (d + cost, v))
50            return False
51
52        answer = -1
53        while l <= r:
54            mid = l + (r - l) // 2
55        
56            if check(mid):
57                answer = mid  
58                l = mid + 1   
59            else:
60                r = mid - 1   
61            
62        return answer