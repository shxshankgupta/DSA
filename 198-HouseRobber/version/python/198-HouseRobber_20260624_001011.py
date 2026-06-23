# Last updated: 6/24/2026, 12:10:11 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n == 1:
5            return nums[0]
6        
7        a = 0
8        b = nums[0]
9        
10        for i in range(1, n):
11            steal = nums[i] + a
12            skip = b
13            
14            c = max(steal, skip)
15            
16            a = b
17            b = c
18            
19        return c