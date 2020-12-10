def sortList(self,head):
    if not head or head.next:
        return head

    slow,fast= head, head.next

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next

    head2=slow.next
    slow.next=None

    leftSort= self.sortList(head)
    rightSort=self.sortList(head2)
    return self.merge(leftSort,rightSort)

def merge(self, left, right):
    final=dummy=ListNode(0)

    while left and right:
        if left.val < right.val:
            dummy.next= left
            left=left.next
        else:
            dummy.next=right
            right=right.next
        dummy=dummy.next

    dummy.next=left or right

    return final.next
