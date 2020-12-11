def minDepth(root):
    if not root:
        return 0

    if not root.right or not root.left:
        return 1+max(minDepth(root.left),minDepth(root.right))
    else:
        return 1+min(minDepth(root.left),minDepth(root.right))