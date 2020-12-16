def findKthLargest(self, nums: List[int], k: int) -> int:
    heap=nums[:]
    heapq.heapify(heap)
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heap[0]