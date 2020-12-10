def hasCycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            # detecting the position
            # slow=head
            # while slow !=fast:
            #     slow=slow.next
            #     fast=fast.next
            # return fast
            return True
    return False