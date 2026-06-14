# Last updated: 6/14/2026, 11:54:24 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        stk = []
9        curr = head
10
11        while curr:
12            stk.append(curr.val)
13            curr = curr.next
14
15        maxSum = 0
16        curr = head
17
18        for _ in range(len(stk) // 2):
19            twinSum = curr.val + stk.pop()
20            maxSum = max(maxSum, twinSum)
21            curr = curr.next
22
23        return maxSum
24        