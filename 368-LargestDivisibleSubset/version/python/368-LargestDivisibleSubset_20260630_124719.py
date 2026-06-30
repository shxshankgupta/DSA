# Last updated: 6/30/2026, 12:47:19 PM
1class Solution:
2    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        nums.sort()
5
6        dp = [1] * n
7
8        prev_idx = [-1] * n
9
10        maxlen = 1
11        end_idx = 0
12
13        for i in range(n):
14            for j in range(i):
15                if nums[i] % nums[j] == 0:
16                    if 1 + dp[j] > dp[i]:
17                        dp[i] = 1 + dp[j]
18                        prev_idx[i] = j    
19
20            if dp[i] > maxlen:
21                maxlen = dp[i]
22                end_idx = i
23
24        result = []
25
26        while end_idx != -1:
27            result.append(nums[end_idx])
28            end_idx = prev_idx[end_idx]
29
30        return result
31
32
33