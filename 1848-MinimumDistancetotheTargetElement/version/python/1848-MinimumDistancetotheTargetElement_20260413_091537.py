# Last updated: 4/13/2026, 9:15:37 AM
1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        min_dist = float('inf')
4        
5        for i, num in enumerate(nums):
6            if num == target:
7                current_dist = abs(i - start)
8                if current_dist < min_dist:
9                    min_dist = current_dist
10                    
11        return min_dist