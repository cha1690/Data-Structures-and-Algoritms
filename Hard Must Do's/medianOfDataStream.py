class medianOfDataStream:

    def __init__(self):
        self.small=[]
        # maxHeap with the largest element at the top
        self.large=[]
    #     minHeap with the largest element at the top

    def addNum(self, num):
        if len(self.small)== len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
