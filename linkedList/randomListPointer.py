def randomListPointer(head):
    if not head:
        return

    mapping={}
    curr=head

    while curr:
        mapping[curr]=Node(curr.val,curr.next,curr.random)
        curr=curr.next

    curr=head

    while curr:
        if curr.next:
            mapping[curr].next=mapping[curr.next]
        if curr.random:
            mapping[curr].random= mapping[curr.random]
        curr=curr.next

    return mapping[head]