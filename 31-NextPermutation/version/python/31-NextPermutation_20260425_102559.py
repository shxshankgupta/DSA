# Last updated: 4/25/2026, 10:25:59 AM
1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n = len(nums)
7        pivot = -1
8        
9        for i in range(n - 2, -1, -1):
10            if nums[i] < nums[i + 1]:
11                pivot = i
12                break
13        
14        if pivot != -1:
15            for j in range(n - 1, pivot, -1):
16                if nums[j] > nums[pivot]:
17                    nums[pivot], nums[j] = nums[j], nums[pivot]
18                    break
19        
20        left, right = pivot + 1, n - 1
21        while left < right:
22            nums[left], nums[right] = nums[right], nums[left]
23            left += 1
24            right -= 1