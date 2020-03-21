# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = self.collision_node(head)
        if not node: return None
        while node != head:
            node = node.next
            head = head.next
        return node
        
    def collision_node(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return slow
        return None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        memo = set()
        for node in self.iterable(head, memo):
            if node in memo: return node
        return None
    
    def iterable(self, head, memo):
        while head:
            yield head
            memo.add(head)
            head = head.next