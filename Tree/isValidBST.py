def isValidBST(self, root: TreeNode, lo=float('-inf'), hi=float('inf')) -> bool:
    if not root:
        return True

    if not lo < root.val < hi:
        return False

    return self.isValidBST(root.left, lo, min(hi,root.val)) and self.isValidBST(root.right, max(root.val, lo), hi )