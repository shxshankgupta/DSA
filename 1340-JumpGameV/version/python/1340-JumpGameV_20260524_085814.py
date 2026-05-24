# Last updated: 5/24/2026, 8:58:14 AM
1class Solution:
2    def maxJumps(self, arr: List[int], d: int) -> int:
3        n = len(arr)
4        memo = [-1] * n
5        
6        def dfs(i):
7            if memo[i] != -1:
8                return memo[i]
9            
10            max_visited = 1
11            
12            for x in range(1, d + 1):
13                j = i + x
14                if j >= n or arr[j] >= arr[i]:
15                    break
16                max_visited = max(max_visited, 1 + dfs(j))
17                
18            for x in range(1, d + 1):
19                j = i - x
20                if j < 0 or arr[j] >= arr[i]:
21                    break
22                max_visited = max(max_visited, 1 + dfs(j))
23                
24            memo[i] = max_visited
25            return memo[i]
26        
27        ans = 0
28        for i in range(n):
29            ans = max(ans, dfs(i))
30            
31        return ans