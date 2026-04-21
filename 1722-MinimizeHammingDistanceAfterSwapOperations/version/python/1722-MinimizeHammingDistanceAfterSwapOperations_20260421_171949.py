# Last updated: 4/21/2026, 5:19:49 PM
1from collections import defaultdict, Counter
2
3class Solution:
4    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
5        n = len(source)
6        parent = list(range(n))
7        
8        def find(i):
9            if parent[i] == i:
10                return i
11            parent[i] = find(parent[i])
12            return parent[i]
13        
14        def union(i, j):
15            root_i = find(i)
16            root_j = find(j)
17            if root_i != root_j:
18                parent[root_i] = root_j
19                
20        for a, b in allowedSwaps:
21            union(a, b)
22            
23        components = defaultdict(list)
24        for i in range(n):
25            components[find(i)].append(i)
26            
27        hamming_distance = 0
28        
29        for indices in components.values():
30            source_counts = Counter(source[i] for i in indices)
31            match_count = 0
32            
33            for i in indices:
34                val = target[i]
35                if source_counts[val] > 0:
36                    match_count += 1
37                    source_counts[val] -= 1
38            
39            hamming_distance += (len(indices) - match_count)
40            
41        return hamming_distance