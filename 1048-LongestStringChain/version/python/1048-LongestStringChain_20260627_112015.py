# Last updated: 6/27/2026, 11:20:15 AM
1class Solution:
2    def longestStrChain(self, words: list[str]) -> int:
3        n = len(words)
4        
5        words.sort(key=len) 
6        
7        dp = [[-1] * (n + 1) for _ in range(n)]
8        
9        def isPredecessor(wordi: str, wordj: str) -> bool:
10            il = len(wordi)
11            jl = len(wordj)
12            
13            if jl - il != 1: 
14                return False
15                
16            i, j = 0, 0  
17            while i < il and j < jl:
18                if wordi[i] == wordj[j]:
19                    i += 1
20                j += 1
21            return i == il
22
23        def solve(i, p):
24            if i >= n:
25                return 0
26            if dp[i][p + 1] != -1:
27                return dp[i][p + 1]
28            
29            skip = solve(i + 1, p)
30            
31            take = 0
32            if p == -1 or isPredecessor(words[p], words[i]):
33                take = 1 + solve(i + 1, i)
34                
35            dp[i][p + 1] = max(skip, take)
36            return dp[i][p + 1]
37
38        return solve(0, -1)