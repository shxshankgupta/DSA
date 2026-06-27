# Last updated: 6/27/2026, 11:37:34 AM
1from collections import Counter
2
3class Solution:
4    def maximumLength(self, nums: List[int]) -> int:
5        count = Counter(nums)
6        max_len = 1 
7        
8        if 1 in count:
9            c = count[1]
10            max_len = max(max_len, c if c % 2 != 0 else c - 1)
11            
12        for num in count:
13            if num == 1:
14                continue
15                
16            current_len = 0
17            x = num
18            
19            while x in count and count[x] >= 2:
20                current_len += 2
21                x = x * x
22                
23            if x in count and count[x] >= 1:
24                current_len += 1
25            else:
26                current_len -= 1
27                
28            max_len = max(max_len, current_len)
29            
30        return max_len