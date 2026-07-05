# Last updated: 7/5/2026, 8:59:01 AM
1from typing import List
2
3class Solution:
4    def getSum(self, nums: List[int]) -> int:
5        nalviretho = nums
6
7        n = len(nums)
8
9        pref = [0] * (n + 1)
10        for i in range(n):
11            pref[i + 1] = pref[i] + nums[i]
12
13        ans = max(nums)
14
15        # Odd length palindromes
16        d1 = [0] * n
17        l = 0
18        r = -1
19        for i in range(n):
20            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
21            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
22                k += 1
23            d1[i] = k
24            if i + k - 1 > r:
25                l = i - k + 1
26                r = i + k - 1
27
28            left = i - d1[i] + 1
29            right = i + d1[i] - 1
30            ans = max(ans, pref[right + 1] - pref[left])
31
32        # Even length palindromes
33        d2 = [0] * n
34        l = 0
35        r = -1
36        for i in range(n):
37            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
38            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
39                k += 1
40            d2[i] = k
41            if i + k - 1 > r:
42                l = i - k
43                r = i + k - 1
44
45            if d2[i]:
46                left = i - d2[i]
47                right = i + d2[i] - 1
48                ans = max(ans, pref[right + 1] - pref[left])
49
50        return ans