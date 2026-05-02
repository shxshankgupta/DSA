# Last updated: 5/2/2026, 10:14:12 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        good_nodes = 0
10
11        stk = [(root, float('-inf'))]
12        while stk : 
13            node, largest = stk.pop()
14
15            if largest <= node.val: 
16                good_nodes += 1
17
18            largest = max(largest, node.val)
19
20            if node.right : 
21                stk.append((node.right, largest))
22            if node.left : 
23                stk.append((node.left, largest))
24
25        return good_nodes