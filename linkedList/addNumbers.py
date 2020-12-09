def addNumbers(l1,l2):
    carry=0
    ans=n=ListNode(0)

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val,carry = divmod(v1+v2+carry, 10)

        n.next= ListNode(val)
        n=n.next

        l1=l1.next if l1 else None
        l2=l2.next if l2 else None

    return ans.next