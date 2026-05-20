# Last updated: 5/20/2026, 6:54:41 AM
1class Solution:
2    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
3        n = len(A)
4        res = [0] * n
5        freq = [0] * (n + 1)
6        common_count = 0
7        
8        for i in range(n):
9            freq[A[i]] += 1
10            if freq[A[i]] == 2:
11                common_count += 1
12                
13            freq[B[i]] += 1
14            if freq[B[i]] == 2:
15                common_count += 1
16                
17            res[i] = common_count
18            
19        return res