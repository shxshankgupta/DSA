# Last updated: 5/3/2026, 8:27:29 AM
1class Solution:
2    def countOppositeParity(self, nums: List[int]) -> List[int]:
3        result = [0] * len(nums)
4        evens = sum(1 for x in nums if x % 2 == 0)
5        odds = len(nums) - evens
6        
7        for i in range(len(nums)):
8            if nums[i] % 2 == 0:
9                evens -= 1
10                result[i] = odds
11            else:
12                odds -= 1
13                result[i] = evens
14                
15        return result