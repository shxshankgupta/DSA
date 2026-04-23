# Last updated: 4/23/2026, 7:22:12 PM
1from typing import List
2
3class Solution:
4    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
5        
6        n = len(nums)
7        MOD = 10**9 + 7
8        # Square root threshold
9        B = int(n**0.5)
10        
11        # small_updates[k][offset] stores a difference-array style log 
12        # of multipliers for strides k <= B.
13        # However, since we deal with multiplication, we use a prefix-product 
14        # approach or process them per (k, offset).
15        small_updates = {} # (k, offset) -> list of (index_in_stride, multiplier)
16
17        for l, r, k, v in queries:
18            if v == 1: continue # Multiplier 1 does nothing
19            
20            if k > B:
21                # Large stride: Update directly
22                for i in range(l, r + 1, k):
23                    nums[i] = (nums[i] * v) % MOD
24            else:
25                # Small stride: Store for batch processing
26                offset = l % k
27                if (k, offset) not in small_updates:
28                    small_updates[(k, offset)] = []
29                # We store l and r to know the range within this specific stride-chain
30                small_updates[(k, offset)].append((l, r, v))
31
32        # Process small stride updates
33        for (k, offset), updates in small_updates.items():
34            # Create a difference array for this specific chain
35            # Chain indices: offset, offset + k, offset + 2k, ...
36            chain_len = (n - 1 - offset) // k + 1
37            diff = [1] * (chain_len + 1)
38            
39            for l, r, v in updates:
40                L = (l - offset) // k
41                R = (r - offset) // k
42                diff[L] = (diff[L] * v) % MOD
43                # Modular inverse is needed for the "end" of the range in a diff array
44                # Since MOD is prime, we use Fermat's Little Theorem: v^(MOD-2)
45                inv_v = pow(v, MOD - 2, MOD)
46                diff[R + 1] = (diff[R + 1] * inv_v) % MOD
47            
48            # Sweep the difference array to apply multipliers
49            curr_mul = 1
50            for j in range(chain_len):
51                curr_mul = (curr_mul * diff[j]) % MOD
52                idx = offset + j * k
53                nums[idx] = (nums[idx] * curr_mul) % MOD
54
55        # Calculate final XOR
56        res = 0
57        for x in nums:
58            res ^= x
59        return res