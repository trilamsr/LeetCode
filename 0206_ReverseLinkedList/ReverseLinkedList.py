# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = collections.deque([(root, sum-root.val)])
        while stack:
            cur, val = stack.popleft()
            if val == 0 and not cur.left and not cur.right: return True
            if cur.left: stack.append((cur.left, val-cur.left.val))
            if cur.right: stack.append((cur.right, val-cur.right.val))
        return False

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recurse(pre, cur):
            if not cur: return pre
            end = recurse(cur, cur.next)
            cur.next = pre
            return end
        return recurse(None, head)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        pre, cur, post = None, head, head.next
        while post:
            cur.next, pre, cur, post = pre, cur, post, post.next
        cur.next = pre
        return cur
        
        
        
        
        
        

