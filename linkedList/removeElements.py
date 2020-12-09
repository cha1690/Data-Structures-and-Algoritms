def removeElements(head, val):
    while head is not None and head.val == val:
        head=head.next

    curr=head

    while curr:
        if curr.next is not None and curr.next.val == val:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head