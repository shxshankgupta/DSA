# Last updated: 4/15/2026, 1:14:41 PM
1class Solution:
2    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
3        n = len(words)
4        min_dist = float('inf')
5        
6        for i in range(n):
7            if words[i] == target:
8                abs_diff = abs(i - startIndex)
9                current_dist = min(abs_diff, n - abs_diff)
10                min_dist = min(min_dist, current_dist)
11        
12        return min_dist if min_dist != float('inf') else -1