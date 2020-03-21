# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ret = ListNode(math.inf)
        cur = ret
        for head, size in self.group_by(head):
            if size == 1:
                cur.next = head
                cur = cur.next
        cur.next = None
        return ret.next
    
    def group_by(self, node):
        if not node: return None, 0
        while node:
            cur, size = node, 1
            while cur.next and node.val == cur.next.val:
                cur = cur.next
                size += 1
            yield node, size
            node = cur.next
            
import itertools
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(math.inf)
        cur = dummy
        group_key = lambda x: x.val
        for k, v in itertools.groupby(self.iterable(head), key=group_key):
            if len(list(v)) == 1:
                cur.next = ListNode(k)
                cur = cur.next
        return dummy.next
            
    def iterable(self, node):
        while node:
            yield node
            node = node.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(val = math.inf)
        dummy.next, cur = head, dummy
        while cur:
            cur.next = self.distinct(cur.next)
            cur = cur.next
        return dummy.next

    def distinct(self, head):
        if not head: return None
        count, val = 1, head.val
        while head.next and head.next.val == val:
            head = head.next
            count += 1
        return head if count == 1 else self.distinct(head.next)