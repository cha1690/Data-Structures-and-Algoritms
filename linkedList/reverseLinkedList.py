def reverse(head):
    prev,curr= None, head

    while curr:
        curr.next,prev,curr  = prev, curr, curr.next
    return prev