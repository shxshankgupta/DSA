# Last updated: 5/6/2026, 11:36:13 AM
1import heapq
2
3class Solution:
4    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
5        heap = []
6        for x, y in points:
7            dist = x**2 + y**2
8            heap.append((dist, [x, y]))
9        
10        heapq.heapify(heap)
11        
12        res = []
13        for _ in range(k):
14            res.append(heapq.heappop(heap)[1])
15            
16        return res