# Last updated: 5/14/2026, 8:06:57 AM
1class Solution:
2    def isGood(self, nums: List[int]) -> bool:
3        n = len(nums) - 1
4        if n < 1:
5            return False
6        
7        count = Counter(nums)
8        
9        for i in range(1, n):
10            if count[i] != 1:
11                return False
12        
13        return count[n] == 2