# Last updated: 6/17/2026, 10:50:44 PM
1class Solution:
2    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
3        if len(connections) < n-1 :
4            return -1
5
6        components = n
7        
8        parent = [i for i in range(n)]
9        rank = [0] * n
10
11        def find (x):
12            if x != parent[x]:
13                parent[x] = find(parent[x])
14
15            return parent[x] 
16
17        def union(x, y):
18            x_parent = find(x)
19            y_parent = find(y)
20
21            if x_parent != y_parent:
22                if rank[x_parent] > rank[y_parent]:
23                    parent[y_parent] = x_parent
24
25                elif rank[x_parent] < rank[y_parent]:
26                    parent[x_parent] = y_parent
27                
28                else:
29                    parent[x_parent] = y_parent
30                    rank[y_parent] += 1
31
32                
33        for con in connections:
34            if find(con[0]) != find(con[1]):
35                union(con[0], con[1])
36                components -= 1
37            else:
38                continue
39        
40        return components - 1