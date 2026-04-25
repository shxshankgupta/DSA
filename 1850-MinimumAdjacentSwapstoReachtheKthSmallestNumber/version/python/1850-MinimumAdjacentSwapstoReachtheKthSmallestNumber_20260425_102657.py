# Last updated: 4/25/2026, 10:26:57 AM
1class Solution:
2    def getMinSwaps(self, num: str, k: int) -> int:
3        target = list(num)
4        for _ in range(k):
5            self.nextPermutation(target)
6        
7        original = list(num)
8        swaps = 0
9        n = len(original)
10        
11        for i in range(n):
12            if original[i] != target[i]:
13                j = i + 1
14                while original[j] != target[i]:
15                    j += 1
16                
17                while j > i:
18                    original[j], original[j-1] = original[j-1], original[j]
19                    swaps += 1
20                    j -= 1
21        
22        return swaps
23
24    def nextPermutation(self, nums: list) -> None:
25        n = len(nums)
26        i = n - 2
27        while i >= 0 and nums[i] >= nums[i + 1]:
28            i -= 1
29        
30        if i >= 0:
31            j = n - 1
32            while nums[j] <= nums[i]:
33                j -= 1
34            nums[i], nums[j] = nums[j], nums[i]
35        
36        nums[i + 1:] = reversed(nums[i + 1:])