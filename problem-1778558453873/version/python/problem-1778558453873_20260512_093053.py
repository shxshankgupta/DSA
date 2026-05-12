# Last updated: 5/12/2026, 9:30:53 AM
1class Solution:
2    def minimumEffort(self, tasks: List[List[int]]) -> int:
3        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
4        
5        min_initial_energy = 0
6        current_energy = 0
7        
8        for actual, minimum in tasks:
9            if current_energy < minimum:
10                min_initial_energy += (minimum - current_energy)
11                current_energy = minimum
12            current_energy -= actual
13            
14        return min_initial_energy