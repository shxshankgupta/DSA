# Last updated: 5/2/2026, 10:42:02 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
10        stack = []
11        curr = root
12        
13        while stack or curr:
14            while curr:
15                stack.append(curr)
16                curr = curr.left
17            
18            curr = stack.pop()
19            k -= 1
20            if k == 0:
21                return curr.val
22            
23            curr = curr.right