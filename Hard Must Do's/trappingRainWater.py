def trapping(arr):
    leftArr=[0]*len(arr)
    rightArr=[0]*len(arr)
    maxLeft=maxRight=water=0
    for i in range(len(arr)):
        maxLeft=max(maxLeft, leftArr[i])
        leftArr[i]= maxLeft

    for i in range(len(arr)-1,-1,-1):
        maxRight = max(maxRight, rightArr[i])
        rightArr[i] = maxRight

    for i in range(len(arr)):
        water+= (min(leftArr[i], rightArr[i])) - arr[i]

    return water