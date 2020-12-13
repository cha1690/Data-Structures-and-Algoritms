def subTree(s,t):
    if isMatch(s,t):
        return True
    if not s:
        return False
    return subTree(s.right,t) or subTree(s.left,t)

def isMatch(s,t):
    if not s and not t:
        return s==t
    return (s.val == t.val) and isMatch(s.right,t.right) and isMatch(s.left,t.left)


