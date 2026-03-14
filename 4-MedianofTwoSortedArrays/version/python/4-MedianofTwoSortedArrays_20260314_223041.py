# Last updated: 3/14/2026, 10:30:41 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
3        if len(nums1) > len(nums2):
4            return self.findMedianSortedArrays(nums2, nums1)
5        
6        n1, n2 = len(nums1), len(nums2)
7        low, high = 0, n1
8        total_length = n1 + n2
9        
10        while low <= high:
11            partitionX = (low + high) // 2
12            partitionY = (n1 + n2 + 1) // 2 - partitionX
13            
14            l1 = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
15            r1 = float('inf') if partitionX == n1 else nums1[partitionX]
16            
17            l2 = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
18            r2 = float('inf') if partitionY == n2 else nums2[partitionY]
19            
20            if l1 <= r2 and l2 <= r1:
21                if total_length % 2 == 0:
22                    return (max(l1, l2) + min(r1, r2)) / 2.0
23                else:
24                    return max(l1, l2)
25            
26            elif l1 > r2:
27                high = partitionX - 1
28            else:
29                low = partitionX + 1
30                
31        return 0.0