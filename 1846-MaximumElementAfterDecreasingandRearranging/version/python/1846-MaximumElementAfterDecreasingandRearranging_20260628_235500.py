# Last updated: 6/28/2026, 11:55:00 PM
1class Solution:
2    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
3        arr.sort()
4        
5        arr[0] = 1
6        for i in range(1, len(arr)):
7            if arr[i] - arr[i - 1] > 1:
8                arr[i] = arr[i - 1] + 1
9
10        return arr[-1]