# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        less_head, bigger_head = ListNode(-1), ListNode(-1)
        less_prev, bigger_prev = less_head, bigger_head
        while head:
            if head.val < x:
                less_prev.next = head
                less_prev = less_prev.next
            else:
                bigger_prev.next = head
                bigger_prev = bigger_prev.next

            head = head.next

        less_prev.next = bigger_prev.next = None
        less_prev.next = bigger_head.next

        return less_head.next