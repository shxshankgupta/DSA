# Last updated: 4/14/2026, 10:04:47 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: TreeNode) -> bool:
9        return self.check_height(root) != -1
10
11    def check_height(self, node):
12        if not node:
13            return 0
14        
15        left_h = self.check_height(node.left)
16        if left_h == -1: 
17            return -1
18            
19        right_h = self.check_height(node.right)
20        if right_h == -1: 
21            return -1
22        
23        if abs(left_h - right_h) > 1:
24            return -1
25            
26        return 1 + max(left_h, right_h)