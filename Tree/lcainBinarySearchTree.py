def lca(root,p,q):
    if not root:
        return

    if root.val == p or root.val == q:
        return root

    if p< root.val and q<root.val:
        return lca(root.left,p,q)
    if p> root.val and q>root.val:
        return lca(root.right,p,q)
    else:
        root