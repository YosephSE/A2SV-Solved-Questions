# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        sizeA = 0
        sizeB = 0
        cur = headA
        while cur:
            sizeA += 1
            cur = cur.next
        cur = headB
        while cur:
            sizeB += 1
            cur = cur.next

        diff = sizeB - sizeA

        while diff > 0:
            headB = headB.next
            diff -= 1
        while diff < 0:
            headA = headA.next
            diff += 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


        
        



        