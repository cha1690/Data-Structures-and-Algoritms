def kthSmallest(matrix, k):
    minHeap=[]

    for i in range(len(matrix)):
        heapq.heappush(minHeap,(matrix[i][0],i,0))

    numberCount=0
    while minHeap:
        number,row,col=heapq.heappop(minHeap)
        if numberCount == k:
            return number
        while col+1 < len(matrix[0]):
            heapq.heappush(minHeap,(matrix[row][col+1],row,col+1))




