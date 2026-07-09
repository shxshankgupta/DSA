# Last updated: 7/9/2026, 9:32:36 PM
1class Solution:
2    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
3        components = [0] * n
4        compId = 0
5
6        for i in range(n-1):
7            if abs(nums[i] - nums[i+1]) > maxDiff:
8                compId += 1
9            components[i+1] = compId
10
11        answer = []
12        for u, v in queries:
13            if components[u] == components[v]:
14                answer.append(True)
15            else:
16                answer.append(False)
17        
18        return answer
19
20