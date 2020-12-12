def traversal(inorder,preorder):
    if inorder:
        index=inorder.index(preorder.pop(0))
        root=TreeNode(inorder[index])
        root.left=traversal(inorder[:index], preorder)
        root.right=traversal(inorder[index+1:], preorder)

        return root