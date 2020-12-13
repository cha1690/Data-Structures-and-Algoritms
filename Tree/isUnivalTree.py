def isUnivalTree(root):
    if not root:
        return True

    if root.right:
        if root.val != root.right.val:
            return False
    if root.left:
        if root.val!= root.left.val:
            return False

    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)