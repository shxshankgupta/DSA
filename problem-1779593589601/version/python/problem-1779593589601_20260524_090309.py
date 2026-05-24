# Last updated: 5/24/2026, 9:03:09 AM
1class Solution:
2    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
3        curr = 0
4        for i in range(len(nums)):
5            if curr < k or nums[i] != nums[curr-k]:
6                nums[curr] = nums[i]
7                curr += 1
8
9        return nums[:curr]