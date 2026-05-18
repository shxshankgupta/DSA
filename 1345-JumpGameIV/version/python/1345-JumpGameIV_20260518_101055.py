# Last updated: 5/18/2026, 10:10:55 AM
1from collections import defaultdict, deque
2
3class Solution:
4    def minJumps(self, arr: list[int]) -> int:
5        n = len(arr)
6        if n <= 1:
7            return 0
8        
9        graph = defaultdict(list)
10        for i, val in enumerate(arr):
11            graph[val].append(i)
12
13        queue = deque([(0, 0)])
14        visited = {0}
15        
16        while queue:
17            idx, steps = queue.popleft()
18            
19            if idx == n - 1:
20                return steps
21            
22            neighbors = []
23            
24            if idx - 1 >= 0:
25                neighbors.append(idx - 1)
26            if idx + 1 < n:
27                neighbors.append(idx + 1)
28             
29            if arr[idx] in graph:
30                neighbors.extend(graph[arr[idx]])
31                del graph[arr[idx]] 
32                
33            for neighbor in neighbors:
34                if neighbor not in visited:
35                    visited.add(neighbor)
36                    queue.append((neighbor, steps + 1))
37                    
38        return 0