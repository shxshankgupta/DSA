# Last updated: 3/15/2026, 9:32:49 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseList(self, head: ListNode) -> ListNode:
9        prev, curr = None, head
10
11        while curr:
12            temp = curr.next
13            curr.next = prev
14            prev = curr
15            curr = temp
16        return prev