# Last updated: 4/28/2026, 10:41:42 AM
1class Solution:
2    def minOperations(self, grid: List[List[int]], x: int) -> int:
3        nums = []
4        for row in grid:
5            nums.extend(row)
6        
7        nums.sort()
8    
9        remainder = nums[0] % x
10        for val in nums:
11            if val % x != remainder:
12                return -1
13        
14        median = nums[len(nums) // 2]
15        
16        total_ops = 0
17        for val in nums:
18            total_ops += abs(val - median) // x
19            
20        return total_ops