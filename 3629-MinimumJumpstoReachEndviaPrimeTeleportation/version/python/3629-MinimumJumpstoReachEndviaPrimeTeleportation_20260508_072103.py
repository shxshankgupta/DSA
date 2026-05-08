# Last updated: 5/8/2026, 7:21:03 AM
1import collections
2
3class Solution:
4    def minJumps(self, nums: List[int]) -> int:
5        n = len(nums)
6        if n == 1:
7            return 0
8        
9        max_num = max(nums)
10        is_prime = [True] * (max_num + 1)
11        is_prime[0] = is_prime[1] = False
12        for p in range(2, int(max_num**0.5) + 1):
13            if is_prime[p]:
14                for i in range(p * p, max_num + 1, p):
15                    is_prime[i] = False
16        
17        prime_to_indices = collections.defaultdict(list)
18        for i, val in enumerate(nums):
19            temp = val
20            d = 2
21            while d * d <= temp:
22                if temp % d == 0:
23                    prime_to_indices[d].append(i)
24                    while temp % d == 0:
25                        temp //= d
26                d += 1
27            if temp > 1:
28                prime_to_indices[temp].append(i)
29
30        queue = collections.deque([(0, 0)])
31        visited_indices = {0}
32        visited_primes = set()
33        
34        while queue:
35            curr_idx, dist = queue.popleft()
36            
37            if curr_idx == n - 1:
38                return dist
39            
40            for neighbor in [curr_idx - 1, curr_idx + 1]:
41                if 0 <= neighbor < n and neighbor not in visited_indices:
42                    visited_indices.add(neighbor)
43                    queue.append((neighbor, dist + 1))
44            
45            val = nums[curr_idx]
46            if val <= max_num and is_prime[val] and val not in visited_primes:
47                visited_primes.add(val)
48                for next_idx in prime_to_indices[val]:
49                    if next_idx not in visited_indices:
50                        visited_indices.add(next_idx)
51                        queue.append((next_idx, dist + 1))
52                prime_to_indices[val] = []
53                
54        return -1