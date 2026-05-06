# Last updated: 5/6/2026, 7:45:42 PM
1import heapq
2from collections import Counter, deque
3
4class Solution:
5    def leastInterval(self, tasks: list[str], n: int) -> int:
6        count = Counter(tasks)
7        maxHeap = [-cnt for cnt in count.values()]
8        heapq.heapify(maxHeap)
9        
10        time = 0
11        q = deque() 
12
13        while maxHeap or q:
14            time += 1
15
16            if maxHeap:
17                cnt = 1 + heapq.heappop(maxHeap)
18                if cnt != 0:
19                    q.append([cnt, time + n])
20                    
21            if q and q[0][1] == time:
22                heapq.heappush(maxHeap, q.popleft()[0])
23        
24        return time