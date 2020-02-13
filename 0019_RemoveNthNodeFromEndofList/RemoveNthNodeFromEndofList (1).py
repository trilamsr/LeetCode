# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ret, ret.next = ListNode(0), head
        back = front = ret
        while front.next:
            front, n = front.next, n-1
            if n < 0: back = back.next
        if back.next: back.next = back.next.next
        return ret.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ret, ret.next = ListNode(0), head
        def recurse(back, front, k):
            if not front.next:
                back.next = back.next.next
                return ret.next
            if k: recurse(back, front.next, k-1) 
            else: return recurse(back.next, front.next, 0)
        return recurse(ret, ret, n)