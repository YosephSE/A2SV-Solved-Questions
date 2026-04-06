class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        l = dummy
        r = dummy

        # move r n+1 steps ahead
        for _ in range(n + 1):
            r = r.next
        
        # move both until r hits the end
        while r:
            l = l.next
            r = r.next
        
        # delete the node
        l.next = l.next.next
        
        return dummy.next