# Last updated: 5/19/2026, 2:16:54 PM
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
16
17        def match(p, q):
18            if not p and not q: return True
19            if not p or not q or p.val != q.val: return False
20            return match(p.right, q.right) and match(p.left, q.left) 
21
22        if not root: return False
23        if match(root, subRoot): return True
24        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)