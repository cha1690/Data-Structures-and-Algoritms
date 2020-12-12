def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.ans=0

    def maxDepth(root):
        if not root:
            return 0
        lroot=maxDepth(root.left)
        rroot=maxDepth(root.right)
        self.ans=max(self.ans, lroot+rroot)
        return 1+max(lroot,rroot)

    maxDepth(root)
    return self.ans