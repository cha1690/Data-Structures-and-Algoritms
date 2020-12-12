def lca(root,p,q):
    if not root:
        return None

    if p==root.val or q==root.val:
        return root

    lroot=lca(root.left,p,q)
    rroot=lca(root.right,p,q)

    if lroot and rroot:
        return root
    return lroot or rroot
