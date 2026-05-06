# Last updated: 5/6/2026, 11:42:32 AM
1import heapq
2
3class Solution:
4    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
5        for i in range(len(points)):
6            x, y = points[i]
7            dist = x**2 + y**2
8            points[i] = (dist, [x, y])
9        
10        heapq.heapify(points)
11        
12        res = []
13        for _ in range(k):
14            res.append(heapq.heappop(points)[1])
15            
16        return res