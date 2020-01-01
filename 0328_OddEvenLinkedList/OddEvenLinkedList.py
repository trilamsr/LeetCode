# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd, even = ListNode(0), ListNode(0)
        ref = [odd, even]
        isEven = 0
        while head:
            ref[isEven].next = head
            ref[isEven] = ref[isEven].next
            head = head.next
            isEven = not isEven
        ref[0].next = even.next
        ref[1].next = None
        return odd.next
        