heap = [-x for x in nums]
heapq.heapify(heap)

while len(heap)>1 and heap[0]!=0:
    heapq.heappush(heap, (heapq.pop(heap)- heapq.pop(heap)))
return -heap[0]