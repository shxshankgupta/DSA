# Last updated: 5/13/2026, 9:22:19 AM
1class Solution:
2    def minMoves(self, nums: List[int], limit: int) -> int:
3        delta = [0] * (2 * limit + 2)
4        n = len(nums)
5        
6        for i in range(n // 2):
7            a, b = nums[i], nums[n - 1 - i]
8            if a > b:
9                a, b = b, a
10            
11            delta[2] += 2
12            delta[a + 1] -= 1
13            delta[a + b] -= 1
14            delta[a + b + 1] += 1
15            delta[b + limit + 1] += 1
16            
17        ans = n
18        curr = 0
19        for i in range(2, 2 * limit + 1):
20            curr += delta[i]
21            if curr < ans:
22                ans = curr
23                
24        return ans