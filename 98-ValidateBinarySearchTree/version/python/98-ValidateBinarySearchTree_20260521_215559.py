# Last updated: 5/21/2026, 9:55:59 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def check(self, root, mn, mx):
9        if not root:
10            return True
11        if root.val < mn or root.val > mx:
12            return False
13        
14        checkLeft = self.check(root.left, mn, root.val - 1)
15        checkRight = self.check(root.right, root.val + 1, mx)
16
17        return checkLeft and checkRight
18
19    def isValidBST(self, root: Optional[TreeNode]) -> bool:            
20        return self.check(root, -10000000000,10000000000)