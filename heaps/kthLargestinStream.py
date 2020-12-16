import heapq

class largestInStream:

    def __init__(self, nums, k):
        self.pool= nums
        self.k = k
        heapq.heapify()
        while len(self.pool) > self.k :
            heapq.heappop(self.pool)

    def add(self,val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        else:
            heapq.heappushpop(self.pool,val)

        return self.pool[0]