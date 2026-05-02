# Last updated: 5/2/2026, 11:56:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9
10class Solution:
11    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
12        if not root:
13            return []
14        
15        result = []
16        queue = deque([root])
17        
18        while queue:
19            level_length = len(queue)
20            
21            for i in range(level_length):
22                node = queue.popleft()
23                
24                # If it's the last node in the current level, add to result
25                if i == level_length - 1:
26                    result.append(node.val)
27                
28                # Add children to the queue for the next level
29                if node.left:
30                    queue.append(node.left)
31                if node.right:
32                    queue.append(node.right)
33                    
34        return result