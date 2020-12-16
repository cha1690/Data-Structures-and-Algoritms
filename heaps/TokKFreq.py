class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1:3,2:2,3:1
        '''
        if k == len(nums):
            return nums

        counter={}
        for num in nums:
            counter[num]= counter.get(num,0)+1

        heap=[]
        for key in counter:
            if len(heap) < k:
                heapq.heappush(heap, (counter[key],key))
            else:
                heapq.heappushpop(heap, (counter[key],key))

        freqK=[]
        while heap:
            freqK.append(heapq.heappop(heap)[1])

        return freqK



