"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        self.interpolate(head)
        self.set_random(head)
        head, copy_head = self.extract(head)
        return copy_head
    
    def extract(self,head):
        copy_head = head.next
        parent, copy = head, head.next
        while copy.next:
            parent.next, copy.next = copy.next, copy.next.next
            parent, copy = parent.next, copy.next
        return head, copy_head
    
    def set_random(self, head):
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next    
        
    def interpolate(self, head):
        while head:
            duplicate = Node(head.val)
            duplicate.next = head.next
            head.next = duplicate
            head = duplicate.next



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        memo = {}
        return self.dfs(head, memo)
    
    def dfs(self, head, memo):
        if not head: return None
        if head in memo: return memo[head]
        node = Node(head.val)
        memo[head] = node
        node.next = self.dfs(head.next, memo)
        node.random = self.dfs(head.random, memo)
        return node
        