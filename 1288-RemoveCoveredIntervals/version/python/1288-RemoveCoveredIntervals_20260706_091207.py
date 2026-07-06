# Last updated: 7/6/2026, 9:12:07 AM
1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: (x[0], -x[1]))
4
5        count = 0
6        current_end = 0
7
8        for start, end in intervals:
9            if end > current_end:
10                count += 1
11                current_end = end 
12                
13        return count