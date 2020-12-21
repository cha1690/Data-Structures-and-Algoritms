def subset(nums):
    res=[]

    def backtrack(subset=[],num_index=0):
        if subset not in res:
            res.append(subset)
        for i in range(num_index, len(nums)):
            backtrack(subset+[nums[i]],i+1)

    backtrack()
    return res