# Last updated: 5/2/2026, 10:47:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        inorder_map = {val: i for i, val in enumerate(inorder)}
10        self.pre_idx = 0
11        
12        def helper(left_idx, right_idx):
13            if left_idx > right_idx:
14                return None
15            
16            root_val = preorder[self.pre_idx]
17            root = TreeNode(root_val)
18            self.pre_idx += 1
19        
20            mid = inorder_map[root_val]
21            
22            root.left = helper(left_idx, mid - 1)
23            root.right = helper(mid + 1, right_idx)
24            
25            return root
26            
27        return helper(0, len(inorder) - 1)