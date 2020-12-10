def removeNth(head, val):
    dummy=ListNode(0)
    dummy=head
    slow=fast=dummy

    for _ in range(val):
        slow=slow.next

    while fast and fast.next:
        slow=slow.next
        fast=fast.next

    fast.next=fast.next.next

    return dummy.next
