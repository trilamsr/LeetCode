# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        return self.recurse(head, head.next)
    def recurse(self, pre, cur):
        if not cur: return pre
        post = cur.next
        cur.next = pre
        pre.next = self.recurse(post, post.next) if post else None
        return cur
        
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        head, head.next, head.next.next = head.next, head, self.swapPairs(head.next.next)
        return head