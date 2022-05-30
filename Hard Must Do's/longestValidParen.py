#         loop over the array and add the index for opening braces
# if you find a closing brace, pop from the stack 
        stack= [-1]
        maxlen = 0
        for index, paren in enumerate(s):
            if paren == "(":
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    maxlen = max(maxlen, index-stack[-1])
        return maxlen
