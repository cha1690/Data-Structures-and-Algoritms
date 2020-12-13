def bsttogst(root):
    total=0
    stack=[]
    curr=root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr=curr.right
        curr=stack.pop()
        curr.val+=total
        total=curr.val
        curr=curr.left
    return root