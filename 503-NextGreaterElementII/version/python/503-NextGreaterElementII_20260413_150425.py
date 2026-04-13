# Last updated: 4/13/2026, 3:04:25 PM
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        res = [-1] * n
5        stack = [] 
6
7        for i in range(n * 2):
8            current_num = nums[i % n]
9            while stack and nums[stack[-1]] < current_num:
10                index = stack.pop()
11                res[index] = current_num
12            if i < n:
13                stack.append(i)
14                
15        return res