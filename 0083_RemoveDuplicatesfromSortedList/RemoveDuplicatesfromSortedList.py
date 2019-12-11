class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            temp = cur
            while cur and cur.val == temp.val:
                cur = cur.next
            temp.next = cur
        return head

