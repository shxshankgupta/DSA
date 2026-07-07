# Last updated: 7/7/2026, 12:08:57 PM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        j = 0
4        n = len(strs)
5        m = len(strs[0])
6        count = 0
7
8        while j < m:
9            i = 0
10            while i < n-1:
11                if strs[i+1][j] < strs[i][j]:
12                    count += 1
13                    break
14                i+=1
15            j += 1
16
17        return count
18
19