def nextPointers(root):

    stack=[root]

    while stack:
        curr=stack.pop()
        if curr.right and curr.left:
            curr.left.next=curr.right
            if curr.next:
                curr.right.next=curr.next.left
            stack.append(curr.right)
            stack.append(curr.left)
    return root
