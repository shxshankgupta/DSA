# Last updated: 5/21/2026, 11:36:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
10        self.counter = 0
11        self.result = None
12        
13        def inorder_dfs(node):
14            if not node or self.result is not None:
15                return
16            
17            inorder_dfs(node.left)
18        
19            self.counter += 1
20            if self.counter == k:
21                self.result = node.val
22                return  
23        
24            inorder_dfs(node.right)
25            
26        inorder_dfs(root)
27        return self.result