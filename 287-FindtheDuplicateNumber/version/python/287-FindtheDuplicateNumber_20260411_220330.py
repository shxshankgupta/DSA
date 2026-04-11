# Last updated: 4/11/2026, 10:03:30 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        tortoise = nums[0]
4        hare = nums[0]
5        
6        while True:
7            tortoise = nums[tortoise]
8            hare = nums[nums[hare]]
9            if tortoise == hare:
10                break
11        
12        tortoise = nums[0]
13        while tortoise != hare:
14            tortoise = nums[tortoise]
15            hare = nums[hare]
16            
17        return hare