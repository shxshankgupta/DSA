# Last updated: 5/4/2026, 3:22:43 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8import collections
9class Codec:
10
11    def serialize(self, root):
12        """Encodes a tree to a single string."""
13        if not root:
14            return ""
15        
16        queue = collections.deque([root])
17        res = []
18        
19        while queue:
20            node = queue.popleft()
21            if node:
22                res.append(str(node.val))
23                queue.append(node.left)
24                queue.append(node.right)
25            else:
26                res.append("n")
27        
28        return ",".join(res)
29
30    def deserialize(self, data):
31        """Decodes your encoded data to tree."""
32        if not data:
33            return None
34        
35        nodes = data.split(",")
36        root = TreeNode(int(nodes[0]))
37        queue = collections.deque([root])
38        
39        i = 1
40        while queue and i < len(nodes):
41            parent = queue.popleft()
42            
43            if nodes[i] != "n":
44                left_node = TreeNode(int(nodes[i]))
45                parent.left = left_node
46                queue.append(left_node)
47            i += 1
48            
49            if i < len(nodes) and nodes[i] != "n":
50                right_node = TreeNode(int(nodes[i]))
51                parent.right = right_node
52                queue.append(right_node)
53            i += 1
54            
55        return root
56
57# Your Codec object will be instantiated and called as such:
58# ser = Codec()
59# deser = Codec()
60# ans = deser.deserialize(ser.serialize(root))