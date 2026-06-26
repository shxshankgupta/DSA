# Last updated: 6/26/2026, 10:10:29 PM
1class Solution:
2    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        
5        bit_size = 2 * n + 2
6        bit = [0] * bit_size
7        
8        def update(idx: int, delta: int):
9            while idx < bit_size:
10                bit[idx] += delta
11                idx += idx & (-idx)
12                
13        def query(idx: int) -> int:
14            s = 0
15            while idx > 0:
16                s += bit[idx]
17                idx -= idx & (-idx)
18            return s
19
20        current_pref = 0
21        update(current_pref + n + 1, 1)
22        
23        ans = 0
24        for num in nums:
25            if num == target:
26                current_pref += 1
27            else:
28                current_pref -= 1
29                
30            ans += query(current_pref + n)
31            
32            update(current_pref + n + 1, 1)
33            
34        return ans