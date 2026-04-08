# Last updated: 4/8/2026, 8:43:34 PM
1class Solution:
2    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
3        MOD = 10**9 + 7
4        
5        for l, r, k, v in queries:
6            for i in range(l, r + 1, k):
7                nums[i] = (nums[i] * v) % MOD
8        
9        res = 0
10        for x in nums:
11            res ^= x
12            
13        return res