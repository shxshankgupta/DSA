# Last updated: 5/21/2026, 11:29:51 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
10        result = []
11        
12        def inorder_dfs(node):
13            if not node:
14                return
15            
16            inorder_dfs(node.left)
17            result.append(node.val)
18            inorder_dfs(node.right)
19
20        inorder_dfs(root)
21        
22        return result[k - 1]