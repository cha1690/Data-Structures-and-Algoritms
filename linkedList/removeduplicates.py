
def removeDuplicates(head):
    pre = dummy = ListNode(0)
    curr = dummy.next = head
    while curr:
        if curr.next and curr.val==curr.next.val:
            while curr.next and curr.val==curr.next.val:
                curr = curr.next.next
            pre.next=curr.next
        else:
            pre=pre.next
        curr=curr.next

    return dummy.next

