# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length-2):

            if nums[i]==nums[i-1]: continue
            l,r=i+1,length-1

            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total<0 :
                    l+=1
                elif total>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    if l<r and nums[l]==nums[l+1]:
                        l+=1
                    if l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res

