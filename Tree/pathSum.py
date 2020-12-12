def pathSum(root, sum):

    if not root:
        return False

    if not root.right and not root.left and root.val==sum:
        return True

    sum-=root.val

    return pathSum(root.right,sum) or pathSum(root.left,sum)