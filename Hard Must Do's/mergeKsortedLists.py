def mergeKsortedLists(lists):
    if not lists:
        return 0
    if len(lists)==1:
        return lists[0]

    mid = len(lists)//2

    list1= mergeKsortedLists(lists[:mid])
    list2= mergeKsortedLists(lists[mid:])

    return merge(list1,list2)

def merge(list1, list2):
    result=dummy=ListNode(0)

    while list1 and list2:
        if list1.val < list2.val:
            dummy.next=list1.val
            list1=list1.next
        else:
            dummy.next=list2.val
            list2=list2.next
        dummy=dummy.next

    dummy.next= list1 or list2

    return result.next
