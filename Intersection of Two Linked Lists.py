# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None: return None
        ptrA, ptrB = headA, headB
        cntA, cntB = 1, 1
        while ptrA != ptrB:
            if ptrA.next: ptrA = ptrA.next
            elif cntA == 1:
                ptrA = headB
                cntA = 0
            else: return None
        
            if ptrB.next: ptrB = ptrB.next
            elif cntB == 1:
                ptrB = headA
                cntB = 0
            else: return None
                
        return ptrA