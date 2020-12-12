def tiltTree(root):
    self.ans=0

    def maxDepth(root):
        if not root:
            return 0
        lroot=maxDepth(root.left)
        rroot=maxDepth(root.right)
        self.ans=abs(lroot-rroot)
        return lroot+rroot+root.val

    maxDepth(root)
    return self.ans