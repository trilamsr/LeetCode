# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        list_iter = self.list_iter(head)
        count = self.count(head)
        return self.dfs(list_iter, 0, count-1)
    
    def count(self, head):
        count = 0
        for _ in self.list_iter(head): count += 1
        return count
        
    def list_iter(self, head):
        while head:
            yield head.val
            head = head.next
            
    def dfs(self, it, lo, hi):
        if lo > hi: return None
        mid = (lo+hi)//2
        ret = TreeNode(
            left=self.dfs(it, lo, mid-1),
            val=next(it),
            right=self.dfs(it, mid + 1, hi)
        )
        return ret

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        left, cur, right = self.partition(head)
        node = TreeNode(cur.val)
        node.left = self.sortedListToBST(left)
        node.right = self.sortedListToBST(right)
        return node
    
    def partition(self, llist):
        if not llist.next: return None, llist, None
        slow, cur, fast = None, llist, llist
        while fast and fast.next:
            slow, cur, fast = cur, cur.next, fast.next.next
        slow.next = None
        return llist, cur, cur.next