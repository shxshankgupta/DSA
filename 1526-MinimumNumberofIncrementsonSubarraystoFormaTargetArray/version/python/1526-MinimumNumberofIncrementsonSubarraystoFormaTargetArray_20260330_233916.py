# Last updated: 3/30/2026, 11:39:16 PM
1class Solution:
2    def minNumberOperations(self, target: List[int]) -> int:
3        total_ops = target[0]
4        
5        for i in range(1, len(target)):
6            if target[i] > target[i-1]:
7                total_ops += target[i] - target[i-1]
8        
9        return total_ops