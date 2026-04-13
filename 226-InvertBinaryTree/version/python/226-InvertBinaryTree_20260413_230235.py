# Last updated: 4/13/2026, 11:02:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
10        if not root:
11            return None
12    
13        q = deque([root])
14    
15        while q:
16            node = q.popleft()
17            node.left, node.right = node.right, node.left
18        
19            if node.left:
20                q.append(node.left)
21            if node.right:
22                q.append(node.right)
23            
24        return root