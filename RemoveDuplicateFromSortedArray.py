# Given a sorted array nums, remove the duplicates in-place such that each element appears only once
# and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums):
        cntr = 1

        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[cntr]=nums[i]
                cntr+=1
        return cntr