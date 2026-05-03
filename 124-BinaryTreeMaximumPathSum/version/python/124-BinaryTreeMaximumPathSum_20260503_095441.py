# Last updated: 5/3/2026, 9:54:41 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxPathSum(self, root: Optional[TreeNode]) -> int:
10        self.max_sum = float('-inf')
11        
12        def get_max_gain(node):
13            if not node:
14                return 0
15
16            left_gain = max(get_max_gain(node.left), 0)
17            right_gain = max(get_max_gain(node.right), 0)
18            
19            current_path_sum = node.val + left_gain + right_gain
20            
21            self.max_sum = max(self.max_sum, current_path_sum)
22            return node.val + max(left_gain, right_gain)
23        
24        get_max_gain(root)
25        return self.max_sum