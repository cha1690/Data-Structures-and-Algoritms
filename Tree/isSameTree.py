def isSameTree(p,q):
    if not p and not q:
        return True
    if p and q:
        return (p.val==q.val) and isSameTree(p.right,q.right) and isSameTree(p.left,q.left)
    return False