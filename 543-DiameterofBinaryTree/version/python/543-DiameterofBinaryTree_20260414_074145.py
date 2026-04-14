# Last updated: 4/14/2026, 7:41:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
10        self.max_diameter = 0
11        
12        def dfs(node):
13            if not node:
14                return 0
15            
16            left = dfs(node.left)
17            right = dfs(node.right)
18            
19            self.max_diameter = max(self.max_diameter, left + right)
20            
21            return 1 + max(left, right)
22            
23        dfs(root)
24        return self.max_diameter