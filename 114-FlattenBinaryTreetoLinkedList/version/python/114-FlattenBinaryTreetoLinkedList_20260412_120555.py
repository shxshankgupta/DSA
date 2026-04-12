# Last updated: 4/12/2026, 12:05:55 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        curr = root
13        
14        while curr:
15            if curr.left:
16                last = curr.left
17                while last.right:
18                    last = last.right
19                last.right = curr.right
20                curr.right = curr.left
21                curr.left = None
22            curr = curr.right