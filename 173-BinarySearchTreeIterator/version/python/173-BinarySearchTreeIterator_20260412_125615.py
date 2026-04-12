# Last updated: 4/12/2026, 12:56:15 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class BSTIterator:
8    def __init__(self, root: Optional[TreeNode]):
9        self.stack = []
10        self._push_left(root)
11
12    def _push_left(self, node):
13        """Helper to push all left children of a node onto the stack."""
14        while node:
15            self.stack.append(node)
16            node = node.left
17
18    def next(self) -> int:
19        """
20        Moves the pointer to the right, then returns the number at the pointer.
21        Average O(1) time complexity.
22        """
23        node = self.stack.pop()
24        if node.right:
25            self._push_left(node.right)
26            
27        return node.val
28
29    def hasNext(self) -> bool:
30        """
31        Returns true if there exists a number in the traversal.
32        O(1) time complexity.
33        """
34        return len(self.stack) > 0
35
36
37# Your BSTIterator object will be instantiated and called as such:
38# obj = BSTIterator(root)
39# param_1 = obj.next()
40# param_2 = obj.hasNext()