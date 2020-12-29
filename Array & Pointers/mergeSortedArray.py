def mergeSortArray(arr1,m,arr2,n):
    if not n:
        return
    if not m:
        for i in range(n):
            arr1[i]=arr2[i]

    l=m+n-1
    m-=1
    n-=1

    while n >=0:
        if m<0 or arr1[m] <= arr1[n]:
            arr1[l], arr2[n] = arr2[n], arr1[l]
        else:
            arr1[l], arr2[m] = arr2[m], arr1[l]
    return
