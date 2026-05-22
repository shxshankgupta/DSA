# Last updated: 5/22/2026, 6:55:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxPathSum(self, root: Optional[TreeNode]) -> int:
10        self.maxSum = float('-inf')
11        
12        def solve(node):
13            if not node:
14                return 0
15
16            leftSum = solve(node.left)
17            if leftSum < 0:
18                leftSum = 0
19            rightSum = max(solve(node.right), 0)
20            #if rightSum < 0: 
21                #rightSum = 0
22            
23            current_path_sum = node.val + leftSum + rightSum
24            
25            self.maxSum = max(self.maxSum, current_path_sum)
26            return node.val + max(leftSum, rightSum)
27        
28        solve(root)
29        return self.maxSum