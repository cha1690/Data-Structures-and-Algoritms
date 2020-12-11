def isSymmetric(root):
    if not root:
        return True
    return isEqual(root.left, root.right)

def isEqual(left,right):
    if not left and not right:
        return True
    if left and right:
        return left.val == right.val and isEqual(left.left,right.right) and isEqual(left.right,right.left)
    return False