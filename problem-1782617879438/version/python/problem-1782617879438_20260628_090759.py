# Last updated: 6/28/2026, 9:07:59 AM
1class Solution:
2    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
3        nums.sort(reverse=True)
4        
5        total_sum = 0
6        
7        for i in range(k):
8            current_element = nums[i]
9            if mul > 1:
10                total_sum += current_element * mul
11            else:
12                total_sum += current_element
13            
14            mul -= 1
15            
16        return total_sum