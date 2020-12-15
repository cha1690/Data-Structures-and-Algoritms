def randomListPointer(head):
    if head is not None:
        mapping = collections.defaultdict(lambda: Node(0, None, None))
        mapping[None] = None
        #a node's next/ random is None, their value will be None and not a new Node

        curr = head
        while curr:
            mapping[curr].val = curr.val
            mapping[curr].next = mapping[curr.next]
            mapping[curr].random = mapping[curr.random]
            curr = curr.next
        return mapping[head]

    # if not head:
    #     return
    #
    # mapping={}
    # curr=head
    #
    # while curr:
    #     mapping[curr]=Node(curr.val,curr.next,curr.random)
    #     curr=curr.next
    #
    # curr=head
    #
    # while curr:
    #     if curr.next:
    #         mapping[curr].next=mapping[curr.next]
    #     if curr.random:
    #         mapping[curr].random= mapping[curr.random]
    #     curr=curr.next
    #
    # return mapping[head]