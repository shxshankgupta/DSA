# Last updated: 6/30/2026, 12:45:43 PM
1class Solution:
2    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        nums.sort()
5        
6        dp = [1] * n
7        prev_idx = [-1] * n
8        
9        maxlen = 1
10        end_idx = 0
11        
12        for i in range(n):
13            for j in range(i):
14                if nums[i] % nums[j] == 0:
15                    if 1 + dp[j] > dp[i]:
16                        dp[i] = 1 + dp[j]
17                        prev_idx[i] = j
18                        
19            if dp[i] > maxlen:
20                maxlen = dp[i]
21                end_idx = i
22                
23        result = []
24        while end_idx != -1:
25            result.append(nums[end_idx])
26            end_idx = prev_idx[end_idx]
27            
28        return result