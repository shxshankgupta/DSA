# Last updated: 3/13/2026, 10:52:23 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        if not matrix or not matrix[0]:
4            return False
5            
6        r = len(matrix) 
7        c = len(matrix[0]) 
8        
9        low = 0
10        high = (r * c) - 1
11        
12        while low <= high:
13            mid = (low + high) // 2
14            row = mid // c
15            col = mid % c 
16
17            if matrix[row][col] == target:
18                return True
19            elif matrix[row][col] < target:
20                low = mid + 1
21            else:
22                high = mid - 1
23
24        return False