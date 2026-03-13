# Last updated: 3/13/2026, 8:24:10 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        max_area = 0
5        n = len(heights)
6    
7        for i in range(n):
8            while stack and heights[stack[-1]] >= heights[i]:
9                height = heights[stack.pop()]
10                width = i if not stack else i - stack[-1] - 1
11                max_area = max(max_area, height * width)
12            stack.append(i)
13    
14        while stack:
15            height = heights[stack.pop()]
16            width = n if not stack else n - stack[-1] - 1
17            max_area = max(max_area, height * width)
18        
19        return max_area