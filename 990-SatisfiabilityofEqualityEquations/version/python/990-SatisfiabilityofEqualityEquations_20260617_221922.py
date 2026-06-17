# Last updated: 6/17/2026, 10:19:22 PM
1class Solution:
2    def equationsPossible(self, equations: List[str]) -> bool:
3
4        parent = [i for i in range(26)]
5        rank = [0] * 26
6
7        def find(x):
8            if x != parent[x]:
9                parent[x] = find(parent[x])  
10            return parent[x]
11
12        def union(x, y):
13            x_parent = find(x)
14            y_parent = find(y)
15            
16            if x_parent != y_parent:
17                if rank[x_parent] > rank[y_parent]:
18                    parent[y_parent] = x_parent
19                elif rank[x_parent] < rank[y_parent]:
20                    parent[x_parent] = y_parent
21                else:
22                    parent[x_parent] = y_parent
23                    rank[y_parent] += 1
24
25        for eqn in equations:
26            if eqn[1] == '=':
27
28                u = ord(eqn[0]) - ord('a')
29                v = ord(eqn[3]) - ord('a')
30                union(u, v)
31
32        for eqn in equations:
33            if eqn[1] == '!':
34                u = ord(eqn[0]) - ord('a')
35                v = ord(eqn[3]) - ord('a')
36
37                if find(u) == find(v):
38                    return False
39
40        return True