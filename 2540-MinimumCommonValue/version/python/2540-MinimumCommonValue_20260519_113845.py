# Last updated: 5/19/2026, 11:38:45 AM
1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        i, j= 0,0
4
5        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
6            return -1
7            
8        while i < len(nums1) and j < len(nums2):
9            if nums1[i] == nums2[j]:
10                return nums1[i]
11            if nums1[i] < nums2[j]:
12                i += 1 
13            else:
14                j += 1
15
16        return -1