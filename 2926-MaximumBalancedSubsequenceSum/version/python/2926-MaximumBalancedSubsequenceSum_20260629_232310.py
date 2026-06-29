# Last updated: 6/29/2026, 11:23:10 PM
1class Solution:
2    def maxBalancedSubsequenceSum(self, nums: list[int]) -> int:
3        n = len(nums)
4        transformed = [nums[i] - i for i in range(n)]
5        unique_vals = sorted(list(set(transformed)))
6        rank_map = {val: i + 1 for i, val in enumerate(unique_vals)}
7        
8        bit_size = len(unique_vals) + 1
9        bit = [float('-inf')] * bit_size
10        
11        def update(idx: int, val: int):
12            while idx < bit_size:
13                if val > bit[idx]:
14                    bit[idx] = val
15                idx += idx & (-idx)
16                
17        def query(idx: int) -> int:
18            max_val = float('-inf')
19            while idx > 0:
20                if bit[idx] > max_val:
21                    max_val = bit[idx]
22                idx -= idx & (-idx)
23            return max_val
24
25        result = float('-inf')
26        
27        for i in range(n):
28            val = transformed[i]
29            rank = rank_map[val]
30            
31            prev_max = query(rank)
32            current_sum = nums[i]
33            if prev_max > 0:
34                current_sum += prev_max
35                
36            if current_sum > result:
37                result = current_sum
38            
39            update(rank, current_sum)
40            
41        return result