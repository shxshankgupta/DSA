# Last updated: 5/21/2026, 10:30:48 AM
1class Solution:
2    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
3        prefixes = set()
4        
5        for val in arr1:
6            while val > 0:
7                prefixes.add(val)
8                val //= 10
9        
10        max_length = 0
11        
12        for val in arr2:
13            while val > 0:
14                if val in prefixes:
15                    max_length = max(max_length, len(str(val)))
16                    break
17                val //= 10
18                
19        return max_length