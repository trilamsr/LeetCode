class Solution:
    def merge(self, l1, l2):
        ret = ListNode("dummer")
        runner = ret
        while l1 and l2:
            if l1.val < l2.val:
                runner.next, l1 = l1, l1.next
            else:
                runner.next, l2 = l2, l2.next
            runner = runner.next
        runner.next = l1 or l2
        return ret.next

    def exp_range(self,start, end, step):
        while start < end:
            yield start
            start *= step
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        for step in self.exp_range(1, len(lists), 2):
            for i in range(0, len(lists)-step, 2*step):
                lists[i] = self.merge(lists[i], lists[i+step])
        return lists[0]

        

        
        
        
        