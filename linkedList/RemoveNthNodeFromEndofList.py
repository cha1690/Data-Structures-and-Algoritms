class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy =  ListNode(0, head)
        
        curr=slow=dummy
        
        for _ in range(n):
            curr = curr.next
        
        while curr and curr.next:
            curr = curr.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
        
