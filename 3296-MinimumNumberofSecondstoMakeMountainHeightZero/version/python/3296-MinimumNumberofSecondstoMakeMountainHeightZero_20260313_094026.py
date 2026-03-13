# Last updated: 3/13/2026, 9:40:26 AM
1import math
2
3class Solution:
4    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
5        def can_reduce(T):
6            total_reduced = 0
7            for w in workerTimes:
8                x = int((-1 + math.sqrt(1 + 8 * T / w)) / 2)
9                total_reduced += x
10                if total_reduced >= mountainHeight:
11                    return True
12            return total_reduced >= mountainHeight
13            
14        low = 1
15        high = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
16        ans = high
17        
18        while low <= high:
19            mid = (low + high) // 2
20            if can_reduce(mid):
21                ans = mid
22                high = mid - 1
23            else:
24                low = mid + 1
25                
26        return ans