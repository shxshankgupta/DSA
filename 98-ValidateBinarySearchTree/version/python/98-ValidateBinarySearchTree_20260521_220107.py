# Last updated: 5/21/2026, 10:01:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isValidBST(self, root: Optional[TreeNode]) -> bool:
10        def dfs(node, low, high):
11            if not node:
12                return True
13            if  not (low < node.val < high):
14                return False
15            return dfs(node.left, low, node.val) and dfs(node.right,node.val, high)
16            
17        return dfs(root, float('-inf'), float('inf'))