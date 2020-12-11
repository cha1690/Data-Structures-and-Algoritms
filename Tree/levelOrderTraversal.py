def levelOrderTraversal(root):
    if not root:
        return

    stack=[root]
    res=[]

    while stack:
        temp=[]
        tempq=[]

        for node in stack:
            temp.append(node.val)
            if node.left:
                tempq.append(node.left)
            if node.right:
                tempq.append(node.right)
        stack=tempq
        res.append(temp)

    return res[::-1]