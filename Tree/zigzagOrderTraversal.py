def zigzagLevelOrder(root):
    if not root:
        return []

    res=[]
    stack=[root]
    index=0

    while stack:
        temp=[]
        tempq=[]
        index+=1
        for node in stack:
            temp.append(node.val)
            if node.left:
                tempq.append(node.left)
            if node.right:
                tempq.append(node.right)
        stack=tempq
        if index%2==0:
            temp=temp[::-1]
        res.append(temp)

    return res