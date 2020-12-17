def maxprod(nums):
    maxprod=nums[0]
    minprod=nums[0]
    res=nums[0]
    for i in range(1,len(nums)):
        maxprod, minprod = max(maxprod*nums[i],minprod*nums[i],nums[i]), min(maxprod*nums[i],minprod*nums[i],nums[i])
        res= max(res,maxprod)
    return res