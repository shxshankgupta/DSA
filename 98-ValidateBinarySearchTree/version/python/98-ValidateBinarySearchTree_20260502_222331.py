# Last updated: 5/2/2026, 10:23:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        self.prev = float('-inf')
10        
11        def inorder(node):
12            if not node:
13                return True
14            
15            if not inorder(node.left):
16                return False
17            
18            if node.val <= self.prev:
19                return False
20            self.prev = node.val
21            
22            return inorder(node.right)
23            
24        return inorder(root)