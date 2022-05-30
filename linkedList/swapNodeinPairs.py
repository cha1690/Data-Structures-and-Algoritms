class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        dummy = curr = ListNode(0, head)
        
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            temp = node2.next
            
            curr.next = node2
            node2.next = node1
            node1.next = temp
            
            curr = node1
            
        
        return dummy.next
