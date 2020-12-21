def permutation(nums):
    res=[]
    visited=set()

    def backtrack(subset=[]):
        if len(subset) == len(nums):
            res.append(subset)
        else:
            for i, num in enumerate(nums):
                if i not in visited:
                    visited.add(i)
                    backtrack(subset+[nums[i]])
                    visited.remove(i)

    backtrack()
    return res