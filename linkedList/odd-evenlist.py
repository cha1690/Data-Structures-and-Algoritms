def oddEvenList(head):
    odd=head
    even=eHead=head.next

    while even and even.next:
        odd.next=odd.next.next
        even.next=even.next.next
        odd=odd.next
        even=even.next

    odd.next=eHead

    return head