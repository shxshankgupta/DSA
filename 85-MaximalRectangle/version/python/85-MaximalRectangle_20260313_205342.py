# Last updated: 3/13/2026, 8:53:42 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        max_area = 0
5        n = len(heights)
6        
7        for i in range(n + 1):
8            current_height = heights[i] if i < n else 0
9            
10            while stack and heights[stack[-1]] >= current_height:
11                h = heights[stack.pop()]
12                w = i if not stack else i - stack[-1] - 1
13                max_area = max(max_area, h * w)
14            stack.append(i)
15            
16        return max_area
17
18    def maximalRectangle(self, matrix: List[List[str]]) -> int:
19        if not matrix or not matrix[0]:
20            return 0
21        
22        n = len(matrix)
23        m = len(matrix[0])
24        max_area = 0
25        heights = [0] * m
26        
27        for i in range(n):
28            for j in range(m):
29                if matrix[i][j] == "1":
30                    heights[j] += 1
31                else:
32                    heights[j] = 0
33            row_max_area = self.largestRectangleArea(heights)
34            max_area = max(max_area, row_max_area)
35            
36        return max_area