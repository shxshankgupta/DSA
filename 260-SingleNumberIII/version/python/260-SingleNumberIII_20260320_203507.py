# Last updated: 3/20/2026, 8:35:07 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> List[int]:
3        xor_result = 0
4        for n in nums:
5            xor_result ^= n
6
7        mask = xor_result & -xor_result
8        a, b = 0, 0
9        
10        for n in nums:
11            if n & mask:
12                a ^= n
13            else:
14                b ^= n
15                
16        return [a, b]