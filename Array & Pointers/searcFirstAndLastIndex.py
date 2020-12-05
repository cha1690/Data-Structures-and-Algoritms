class Solution:
    def searchRange(self, nums, target):

        result =[-1,-1]
        result[0] = self.searchFirstIndex(nums, target)
        result[1] = self.searchlastIndex(nums, target)

        return result

    def searchFirstIndex(self, nums, target):

        low, high= 0, len(nums)-1
        while low<=high:
            mid=(low+high)//2

            if target == nums[mid] :
                index = mid
                high = mid-1
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return index

    def searchlastIndex(self, nums, target):

        low, high= 0, len(nums)-1
        while low<=high:
            mid=(low+high)//2

            if target == nums[mid] :
                index = mid
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return index
