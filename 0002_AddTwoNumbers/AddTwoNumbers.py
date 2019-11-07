class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(None)
        runner = ret
        remainder = 0
        while (l1 and l2):
            if (remainder + l1.val + l2.val < 0):
                runner.next = ListNode(remainder+l1.val+l2.val)
                remainder = 0
            else:
                input = (remainder + l1.val + l2.val)%10 
                runner.next = ListNode(input)
                remainder = (remainder + l1.val + l2.val- input)//10
            l1, l2, runner = l1.next, l2.next, runner.next
        postrun = l1 or l2
        while (remainder != 0):
            input = remainder + postrun.val if postrun else remainder
            runner.next = ListNode(input%10)
            remainder, runner = input - input%10, runner.next
            postrun = postrun.next if postrun else postrun
        runner.next = ListNode(remainder) if remainder != 0 else postrun
        return ret.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        curr = ret
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1: total += l1.val
            if l2: total += l2.val
            carry, total = total // 10, total % 10
            curr.next = (l1 or l2) if (l1 or l2) else ListNode(0)
            curr = curr.next
            curr.val = total
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return ret.next