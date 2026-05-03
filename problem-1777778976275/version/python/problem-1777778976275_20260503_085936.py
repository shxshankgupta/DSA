# Last updated: 5/3/2026, 8:59:36 AM
1import bisect
2
3class Solution:
4    def maxFixedPoints(self, nums: list[int]) -> int:
5        
6        candidates = []
7        for i, val in enumerate(nums):
8            if val <= i:
9                candidates.append((i - val, val))
10        candidates.sort()
11        
12        lis_list = []
13        for d, val in candidates:
14            idx = bisect.bisect_left(lis_list, val)
15            if idx == len(lis_list):
16                lis_list.append(val)
17            else:
18                lis_list[idx] = val
19                
20        return len(lis_list)