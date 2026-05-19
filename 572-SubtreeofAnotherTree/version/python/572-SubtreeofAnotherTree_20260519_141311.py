# Last updated: 5/19/2026, 2:13:11 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7# Definition for a binary tree node.
8# class TreeNode:
9#     def __init__(self, val=0, left=None, right=None):
10#         self.val = val
11#         self.left = left
12#         self.right = right
13
14class Solution:
15    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
16        if not root:
17            return False
18        
19        if self.isSameTree(root, subRoot):
20            return True
21        
22        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
23        
24    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
25        if not p and not q:
26            return True
27        if not p or not q:
28            return False
29        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)