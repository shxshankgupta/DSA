# Last updated: 6/15/2026, 10:52:02 PM
1from collections import defaultdict, deque
2
3class Solution:
4    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
5
6        adj = defaultdict(list)
7        indegree = [0] * numCourses
8        
9        for u, v in prerequisites:
10            adj[u].append(v)
11            indegree[v] += 1
12            
13        queue = deque()
14        count = 0 
15        
16        for i in range(numCourses):
17            if indegree[i] == 0:
18                queue.append(i)
19                
20        while queue:
21            u = queue.popleft()
22            
23            for v in adj[u]:
24                indegree[v] -= 1
25                
26                if indegree[v] == 0:
27                    queue.append(v)
28            count += 1
29                    
30        return count == numCourses