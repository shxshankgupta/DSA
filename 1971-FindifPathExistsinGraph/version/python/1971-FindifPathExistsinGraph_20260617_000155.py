# Last updated: 6/17/2026, 12:01:55 AM
1from collections import deque, defaultdict
2
3class Solution:
4    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
5        if source == destination:
6            return True
7        
8        graph = defaultdict(list)
9        for u, v in edges:
10            graph[u].append(v)
11            graph[v].append(u)
12            
13        queue = deque([source])
14        visited = {source}
15        
16        while queue:
17            current_node = queue.popleft()
18            
19            for neighbor in graph[current_node]:
20                if neighbor == destination:
21                    return True
22                
23                if neighbor not in visited:
24                    visited.add(neighbor)
25                    queue.append(neighbor)
26                    
27        return False