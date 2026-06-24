# Last updated: 6/24/2026, 12:13:22 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n == 1:
5            return nums[0]
6
7        a = 0
8        b = nums[0]
9        c = b
10
11        for i in range(2, n):
12            
13            steal = nums[i-1] + a
14            skip = b
15            c = max(steal, skip)
16
17            a = b
18            b = c
19
20        ans1 = c
21
22        a = 0
23        b = 0
24        c = b
25
26        for i in range(2, n+1):
27            
28            steal = nums[i-1] + a
29            skip = b
30            c = max(steal, skip)
31
32            a = b
33            b = c
34
35        ans2 = c
36
37        return max(ans1, ans2)
38