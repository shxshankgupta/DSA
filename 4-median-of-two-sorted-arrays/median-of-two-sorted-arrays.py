class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)
        n = len(num)
        l = n // 2
        if len(num) % 2 == 0:
            return (num[l-1]+num[l]) / 2.0

        return float(num[l])
