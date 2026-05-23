# Last updated: 5/23/2026, 7:50:06 AM
1class Solution:
2    def check(self, nums: list[int]) -> bool:
3        b = sorted(nums)
4    
5        for i in range(len(nums)):
6            if nums[i] == b[0]:
7                
8                reconstructed = nums[i:] + nums[:i]
9                
10                # Check if this completely fixes the rotation
11                if reconstructed == b:
12                    return True
13                    
14        return False