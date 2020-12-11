def inorderTraversal(root):
    res=[]
    helper(root, res)
    return res

def helper(node, res):
    if node:
        helper(node.left, res)
        res.append(node.val)
        helper(node.left, res)

# Solution 2

def inorderTraversal(root):
    res=[]
    curr=root
    stack=[]
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
        curr=stack.pop()
        res.append(curr.val)
        curr=curr.right
    return res
