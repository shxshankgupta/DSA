# Last updated: 6/17/2026, 11:39:02 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        n = len(edges) 
4        parent = [i for i in range(n+1)]
5
6        def find(x):
7            if x == parent[x]:
8                return x
9            parent[x] = find(parent[x])
10            return parent[x]
11
12        def union(x, y):
13            x_parent = find(x)
14            y_parent = find(y)
15
16            if x_parent != y_parent:
17                parent[x_parent] = y_parent
18                return True
19            return False
20
21        for u, v in edges:
22            if not union(u, v):
23                return [u, v]
24
25
26
27