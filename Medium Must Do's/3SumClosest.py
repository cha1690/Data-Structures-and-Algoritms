def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    diff=float('inf')

    for i in range(len(nums)):
        l, r= i+1, len(nums)-1

        while l< r:

            total = nums[l]+nums[i]+nums[r]

            if target == total:
                return total
            elif abs(total-target) < abs(diff-target):
                diff = total
            elif target > total:
                l+=1
            elif target < total:
                r-=1

    return diff