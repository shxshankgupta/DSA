# Last updated: 6/25/2026, 11:30:49 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n = len(nums)
4        # p ranges from -1 to n-1, so we shift its index by +1 in the DP table. SO, Size will be n x (n + 1)
5        dp = [[-1] * (n + 1) for _ in range(n)]
6        
7        def solve(i, p):
8            if i >= n:
9                return 0
10                
11            if dp[i][p + 1] != -1:
12                return dp[i][p + 1]
13            
14            skip = solve(i + 1, p)
15            
16            take = 0
17            if p == -1 or nums[i] > nums[p]:
18                take = 1 + solve(i + 1, i)
19                
20            dp[i][p + 1] = max(take, skip)
21            return dp[i][p + 1]
22            
23        return solve(0, -1)