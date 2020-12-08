def validParen(s):
    stack=[]
    mapping={']':'[','}':'{',')':'('}
    for paren in s:
        if paren in mapping.values():
            stack.append(paren)
        elif (stack.pop() != mapping[paren]) or not stack:
            return False
    return stack==[]