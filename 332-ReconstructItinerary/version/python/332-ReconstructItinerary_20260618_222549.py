# Last updated: 6/18/2026, 10:25:49 PM
1from collections import defaultdict
2
3class Solution:
4    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
5        adj = defaultdict(list)
6        for u, v in tickets:
7            adj[u].append(v)
8
9        for u in adj:
10            adj[u].sort(reverse = True)
11        
12        num_tickets = len(tickets)
13        result = []
14        path = []
15
16        def dfs(airport):
17            while adj[airport]:
18                next_dest = adj[airport].pop() 
19                dfs(next_dest)                 
20                
21            path.append(airport)
22            
23        dfs("JFK")
24
25        return path[:: -1]