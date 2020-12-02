# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# edge cases: negative numbers or zero
# length of the array should always be greater than 2

class Solution:
    def twoSum(self, nums, target):
        complementMap = {}
        for index, num in enumerate(nums):
            compl = target-num
            if compl not in complementMap:
                complementMap[num] = index
            else:
                return [complementMap[compl], index]
        return []

# time: O(n)
# space: O(n)