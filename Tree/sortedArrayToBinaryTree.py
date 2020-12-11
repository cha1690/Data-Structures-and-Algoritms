def sortedArray2BinTree(nums):
    if not nums:
        return

    left,right=0,len(nums)-1
    mid=(left+right)//2

    root=TreeNode(nums[mid])
    root.left=sortedArray2BinTree(nums[:mid])
    root.right=sortedArray2BinTree(nums[mid+1:])

    return root
