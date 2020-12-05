# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    def majorityElement(self, nums):
        counter={}
        for num in nums:
            counter[num] = counter.get(num,0)+1
            if counter[num] > len(nums)//2:
                return num
        return -1