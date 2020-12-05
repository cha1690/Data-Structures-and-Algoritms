class Solution:
    def duplicate(self, nums):
        return len(set(nums)) < len(nums)