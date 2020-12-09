def isPalindrome(head):
    curr = fast = head

    while fast and fast.next:
        curr = curr.next
        fast = fast.next.next

    prev= None

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True