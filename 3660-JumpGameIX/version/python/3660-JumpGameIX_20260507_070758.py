# Last updated: 5/7/2026, 7:07:58 AM
1class Solution:
2    def maxValue(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5        
6        pre_max = [0] * n
7        pre_max[0] = nums[0]
8        for i in range(1, n):
9            pre_max[i] = max(pre_max[i-1], nums[i])
10            
11        suf_min = [0] * n
12        suf_min[n-1] = nums[n-1]
13        for i in range(n-2, -1, -1):
14            suf_min[i] = min(suf_min[i+1], nums[i])
15            
16        res = [0] * n
17        curr_max = 0
18        left = 0
19        for i in range(n):
20            curr_max = max(curr_max, nums[i])
21            if i == n - 1 or pre_max[i] <= suf_min[i+1]:
22                for j in range(left, i + 1):
23                    res[j] = curr_max
24                if i + 1 < n:
25                    curr_max = 0
26                    left = i + 1
27                    
28        return res