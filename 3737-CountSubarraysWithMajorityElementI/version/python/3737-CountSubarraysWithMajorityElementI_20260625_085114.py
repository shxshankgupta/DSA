# Last updated: 6/25/2026, 8:51:14 AM
1class Solution:
2    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        res = 0
5
6        for i in range(n):
7            target_occ = 0
8            length = 0
9
10            for j in range(i, n):
11                length += 1
12                if nums[j] == target:
13                    target_occ += 1
14
15                if target_occ > length // 2:
16                    res += 1
17        
18        return res