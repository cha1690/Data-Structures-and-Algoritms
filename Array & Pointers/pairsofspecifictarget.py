# Find the index of two numbers whose sum equals to target.
# Array is sorted and may have duplicate values. If there multiple such index, return all of them
# Example:
# Input: arr : [1,2,2,3,4,4,5]
#               0,1,2,3,4,5,6
# Output: [[0, 6], [1, 5] ,[1, 4], [2, 5], [2, 4]]


def allSum(nums, target):
    left, right = 0, len(nums)-1
    res=[]
    while left < right:
        total = nums[left]+nums[right]
        if total == target:
            res.append([left,right])
            if (nums[left]==nums[left+1]):
                res.append([left+1,right])
            if (nums[right]==nums[right-1]):
                res.append([left,right-1])
            left+=1
            right-=1
        elif (total > target):
            right -= 1
        else:
            left += 1;
    print(res)

allSum([1,2,2,3,4,4,5],6)