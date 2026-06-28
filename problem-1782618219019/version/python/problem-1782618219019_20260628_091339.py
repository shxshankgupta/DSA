# Last updated: 6/28/2026, 9:13:39 AM
1from typing import List
2
3class Solution:
4    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
5        midway = (occupiedIntervals, freeStart, freeEnd)
6        
7        if not occupiedIntervals:
8            return []
9            
10        occupiedIntervals.sort(key=lambda x: x[0])
11        
12        merged = [occupiedIntervals[0]]
13        for i in range(1, len(occupiedIntervals)):
14            current = occupiedIntervals[i]
15            last_merged = merged[-1]
16            
17            if current[0] <= last_merged[1] + 1:
18                last_merged[1] = max(last_merged[1], current[1])
19            else:
20                merged.append(current)
21                
22        result = []
23        for start, end in merged:
24            if end < freeStart or start > freeEnd:
25                result.append([start, end])
26            else:
27                if start < freeStart:
28                    result.append([start, freeStart - 1])
29                if end > freeEnd:
30                    result.append([freeEnd + 1, end])
31                    
32        return result