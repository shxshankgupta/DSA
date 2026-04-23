# Last updated: 4/23/2026, 7:47:43 AM
1from collections import defaultdict
2from typing import List
3
4class Solution:
5    def distance(self, nums: List[int]) -> List[int]:
6        n = len(nums)
7        res = [0] * n
8        
9        indices_map = defaultdict(list)
10        for i, val in enumerate(nums):
11            indices_map[val].append(i)
12        
13        for val in indices_map:
14            idxs = indices_map[val]
15            m = len(idxs)
16            
17            total_sum = sum(idxs)
18            prefix_sum = 0
19            
20            for i in range(m):
21                current_idx = idxs[i]
22                
23                count_left = i
24                count_right = m - 1 - i
25                
26                suffix_sum = total_sum - prefix_sum - current_idx
27                
28                left_dist = (count_left * current_idx) - prefix_sum
29                right_dist = suffix_sum - (count_right * current_idx)
30                
31                res[current_idx] = left_dist + right_dist
32                
33                prefix_sum += current_idx
34                
35        return res