# Last updated: 7/7/2026, 12:09:34 PM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        n = len(strs)
4        m = len(strs[0])
5        count = 0
6        
7        for j in range(m):
8            for i in range(n - 1):
9                if strs[i+1][j] < strs[i][j]:
10                    count += 1
11                    break 
12                    
13        return count