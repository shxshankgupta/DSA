# Last updated: 5/29/2026, 10:38:10 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
12        if not node:
13            return None
14        
15        old_to_new = {}
16        
17        def dfs(curr_node):
18            if curr_node in old_to_new:
19                return old_to_new[curr_node]
20            
21            clone = Node(curr_node.val)
22            old_to_new[curr_node] = clone
23            
24            for neighbor in curr_node.neighbors:
25                clone.neighbors.append(dfs(neighbor))
26                
27            return clone
28            
29        return dfs(node)