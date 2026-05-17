# Last updated: 5/17/2026, 8:38:39 AM
1class Solution:
2    def canReach(self, arr: List[int], start: int) -> bool:
3        if 0 <= start < len(arr) and arr[start] >= 0:
4            if arr[start] == 0:
5                return True
6            
7            arr[start] = -arr[start]
8            
9            return (self.canReach(arr, start + arr[start]) or 
10                    self.canReach(arr, start - arr[start]))
11        
12        return False