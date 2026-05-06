# Last updated: 5/6/2026, 1:08:05 PM
1import heapq
2class Solution:
3    def findKthLargest(self, nums: List[int], k: int) -> int:
4        for i in range(len(nums)):
5            nums[i] = - nums[i]
6        
7        heapq.heapify(nums)
8        
9        for _ in range(k - 1):
10            heapq.heappop(nums)
11
12        return -nums[0]