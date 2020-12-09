def mergeTwoLists(l1,l2):
    result=n=ListNode(0)

    while l1 and l2:
        if l1.val <l2.val:
            n.next = l1
            l1=l1.next
        else:
            n.next = l2
            l2=l2.next
        n=n.next

    if l1 or l2:
        n.next = l1 or l2

    return result.next