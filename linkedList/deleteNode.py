def delete(node):
    if node:
        node.val = node.next.val
        node.next = node.next.next