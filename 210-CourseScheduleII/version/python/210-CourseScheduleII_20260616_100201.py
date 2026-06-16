# Last updated: 6/16/2026, 10:02:01 AM
1from collections import defaultdict, deque
2
3class Solution:
4    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
5
6        adj = defaultdict(list)
7        indegree = [0] * numCourses
8        
9        # To Build the graph correctly{ u -> v } - for loop me pehle v fir u
10        for v, u in prerequisites:
11            adj[u].append(v)
12            indegree[v] += 1
13
14        q = deque()
15
16        for u in range(numCourses):
17            if indegree[u] == 0:
18                q.append(u)
19
20        res = []
21
22        while q:
23            u = q.popleft()
24            res.append(u)
25
26            for v in adj[u]:
27                indegree[v] -= 1
28
29                if indegree[v] == 0:
30                    q.append(v)
31
32        
33        return res if len(res) == numCourses else []