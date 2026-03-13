# Last updated: 3/13/2026, 10:51:52 AM
1class Solution:
2    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        greater_map = {}
4        helper_stack = []
5
6        for i in range(len(nums2) - 1, -1, -1):
7            num = nums2[i]
8            if not helper_stack:
9                greater_map[num] = -1
10                helper_stack.append(num)
11                continue
12            if helper_stack[-1] > num:
13                greater_map[num] = helper_stack[-1]
14                helper_stack.append(num)
15                continue
16
17            while helper_stack and helper_stack[-1] <= num:
18                helper_stack.pop()
19            if not helper_stack:
20                greater_map[num] = -1
21            else:
22                greater_map[num] = helper_stack[-1]
23
24            helper_stack.append(num)
25            
26        result = [greater_map.get(n, -1) for n in nums1]
27        
28        return result