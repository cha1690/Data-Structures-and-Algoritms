# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].


class Solution:
    def product(self, nums):
        l,r,answer=[1]*len(nums), [1]*len(nums),[1]*len(nums)

        for i in range(1,len(nums)):
            l[i] = l[i-1]*nums[i-1]

        for i in reversed(range(len(nums)-1)):
            r[i] = r[i+1]*nums[i+1]

        for i in range(len(nums)):
            answer[i] = l[i]*r[i]

        return answer