# Last updated: 5/1/2026, 10:48:01 AM
1class Solution:
2    def maxRotateFunction(self, nums: List[int]) -> int:
3        n = len(nums)
4        total_sum = sum(nums)
5        
6        current_f = sum(i * val for i, val in enumerate(nums))
7        max_f = current_f
8        for k in range(1, n):
9            current_f = current_f + total_sum - n * nums[n - k]
10            if current_f > max_f:
11                max_f = current_f
12                
13        return max_f