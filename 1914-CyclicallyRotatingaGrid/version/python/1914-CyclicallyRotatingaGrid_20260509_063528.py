# Last updated: 5/9/2026, 6:35:28 AM
1class Solution:
2    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m, n = len(grid), len(grid[0])
4        num_layers = min(m, n) // 2
5        
6        for layer in range(num_layers):
7            elements = []
8            
9            for j in range(layer, n - 1 - layer):
10                elements.append(grid[layer][j])
11            for i in range(layer, m - 1 - layer):
12                elements.append(grid[i][n - 1 - layer])
13            for j in range(n - 1 - layer, layer, -1):
14                elements.append(grid[m - 1 - layer][j])
15            for i in range(m - 1 - layer, layer, -1):
16                elements.append(grid[i][layer])
17            
18            total_elements = len(elements)
19            net_rotation = k % total_elements
20            rotated_elements = elements[net_rotation:] + elements[:net_rotation]
21            
22            idx = 0
23            for j in range(layer, n - 1 - layer):
24                grid[layer][j] = rotated_elements[idx]
25                idx += 1
26            for i in range(layer, m - 1 - layer):
27                grid[i][n - 1 - layer] = rotated_elements[idx]
28                idx += 1
29            for j in range(n - 1 - layer, layer, -1):
30                grid[m - 1 - layer][j] = rotated_elements[idx]
31                idx += 1
32            for i in range(m - 1 - layer, layer, -1):
33                grid[i][layer] = rotated_elements[idx]
34                idx += 1
35                
36        return grid