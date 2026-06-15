# Last updated: 6/15/2026, 10:04:16 PM
1class Solution:
2
3    def dfs(self, u: int, isConnected: List[List[int]], visited: List[bool], n: int):
4        visited[u] = True
5        for v in range(n):
6            if isConnected[u][v] == 1 and not visited[v]:
7                self.dfs(v, isConnected, visited, n)
8
9    def findCircleNum(self, isConnected: List[List[int]]) -> int:
10        provinces = 0
11        n = len(isConnected)
12        visited = [False] * n
13
14        for u in range(n):
15            if not visited[u]:
16                provinces += 1
17                self.dfs(u, isConnected, visited, n)
18
19        return provinces
20
21