# Last updated: 7/5/2026, 8:47:37 AM
1class Solution:
2    def maxDigitRange(self, nums: list[int]) -> int:
3        max_range = -1
4        ans = 0
5
6        for num in nums:
7            digits = [int(d) for d in str(num)]
8            dig_range = max(digits) - min(digits)
9
10            if dig_range > max_range:
11                max_range = dig_range
12                ans = num
13
14            elif dig_range == max_range:
15                ans += num
16
17
18        return ans