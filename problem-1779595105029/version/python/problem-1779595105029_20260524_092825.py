# Last updated: 5/24/2026, 9:28:25 AM
1class Solution:
2    def minOperations(self, nums: list[int]) -> int:
3        n = len(nums)
4        if n <= 1:
5            return 0
6            
7        idx_zero = nums.index(0)
8        
9        is_increasing = True
10        for i in range(n):
11            if nums[(idx_zero + i) % n] != i:
12                is_increasing = False
13                break
14
15        is_decreasing = True
16        for i in range(n):
17            if nums[(idx_zero - i + n) % n] != i:
18                is_decreasing = False
19                break
20
21        if not is_increasing and not is_decreasing:
22            return -1
23
24        ans = float('inf')
25
26        if is_increasing:
27            opt1 = idx_zero
28            opt2 = 1 + ((n - idx_zero) % n) + 1
29            ans = min(opt1, opt2)
30
31        if is_decreasing:
32            opt3 = ((idx_zero - (n - 1) + n) % n) + 1
33            opt4 = 1 + ((n - 1 - idx_zero) % n)
34            ans = min(ans, opt3, opt4)
35            
36        return ans