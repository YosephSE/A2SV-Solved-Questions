# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        yourSet = set()
        cur = headA
        while cur:
            yourSet.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in yourSet:
                return cur
            cur = cur.next
        return None
        