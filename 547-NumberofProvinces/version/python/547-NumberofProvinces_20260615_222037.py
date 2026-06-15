# Last updated: 6/15/2026, 10:20:37 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        visited = [False] * n
5        provinces = 0
6        
7        def dfs(u, isConnected, visited):
8            visited[u] = True
9            for v in range(n):
10                if isConnected[u][v] == 1 and not visited[v]:
11                    dfs(v, isConnected, visited)
12        
13        for u in range(n):
14            if not visited[u]:
15                provinces += 1
16                dfs(u, isConnected, visited)
17                
18        return provinces