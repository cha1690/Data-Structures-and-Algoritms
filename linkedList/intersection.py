def intersect(headA,headB):
    pA=headA
    pB=headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA