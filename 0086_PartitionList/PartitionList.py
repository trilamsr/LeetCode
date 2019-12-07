# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt = curLT = ListNode('LT')
        gte = curGTE = ListNode('GTE')        
        while head:
            if head.val < x:
                curLT.next = head
                curLT = curLT.next
                print(head.val)
            else:
                curGTE.next = head
                curGTE = curGTE.next
                print(head.val)
            head = head.next
        curGTE.next = None
        curLT.next = gte.next
        return lt.next
            