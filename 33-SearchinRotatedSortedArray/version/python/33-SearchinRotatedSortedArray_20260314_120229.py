# Last updated: 3/14/2026, 12:02:29 PM
1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        return self.modifiedBinarySearch(nums, target, 0, len(nums) - 1)
4
5    def modifiedBinarySearch(self, arr, target, left, right):
6        if left > right:
7            return -1
8        mid = left + ((right - left) // 2)
9        
10
11        if arr[mid] == target:
12            return mid
13
14        if arr[left] <= arr[mid]:
15            if arr[left] <= target <= arr[mid]:
16                return self.modifiedBinarySearch(arr, target, left, mid - 1)
17            else:
18                return self.modifiedBinarySearch(arr, target, mid + 1, right)
19        else:
20            if arr[mid] <= target <= arr[right]:
21                return self.modifiedBinarySearch(arr, target, mid + 1, right)
22            else:
23                return self.modifiedBinarySearch(arr, target, left, mid - 1)