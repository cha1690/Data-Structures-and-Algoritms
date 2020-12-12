def invertTree(root):
    if not root:
        return

    root.left, root.right= self.invertTree(root.right), self.invertTree(root.left)

    return root