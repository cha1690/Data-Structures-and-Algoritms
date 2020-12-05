class Solution:
    def maxSubarray(self,nums):

        while len(nums) >0:
            maxSum = currSum = nums[0]

            for num in nums[1:]:
                maxSum = max(maxSum, currSum)
                currSum = max(num, currSum+num)
        return 0