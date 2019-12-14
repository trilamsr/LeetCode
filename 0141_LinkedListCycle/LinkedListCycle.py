# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: return True
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        mem = set()
        while head and head not in mem:
            mem.add(head)
            head = head.next
        return head in mem