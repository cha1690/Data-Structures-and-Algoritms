# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

class Solution:

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k= k%n

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)