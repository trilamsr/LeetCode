# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return
        a, b = self.split(head)
        b = self.reverse(b)
        self.merge(a, b)
    
    # M_BRAX's Merge
    def merge(self, a, b):
        cur = a
        queue = collections.deque([b, a.next])
        while queue[0]:
            queue.append(queue[0].next)
            cur.next = queue.popleft()
            cur = cur.next

    def merge(self, a, b):
        while a and b:
            a_next, b_next = a.next, b.next
            pre, cur, post = a, b, a.next
            pre.next = cur
            cur.next = post
            a, b = a_next, b_next
        
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            post = cur.next
            cur.next = pre
            pre, cur = cur, post
        return pre
    
    def split(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return head, head2