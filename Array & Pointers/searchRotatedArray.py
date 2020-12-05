# You are given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7]
# might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1.

class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low<=high:
            mid= (low+high)//2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target < nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1


