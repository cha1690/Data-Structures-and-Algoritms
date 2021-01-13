def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    import heapq
    intervals = sorted(intervals, key=lambda x:x[0]) # Sort by start value
    heap = []
    for i in intervals:
        if heap and heap[0] <= i[0]:
            # If the new start time is greater than or equal to the exist end time, means the room has been released, replace the previous time with the new ending time
            heapq.heapreplace(heap, i[-1])
        else:
            # The room is still in use, add (push a new end time to min heap) a new room
            heapq.heappush(heap, i[-1])
    return len(heap)