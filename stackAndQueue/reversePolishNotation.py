def evalRPN(self, tokens: List[str]) -> int:
    stack=[]
    sym=["+","/","-","*"]

    for token in tokens:
        if token not in sym:
            stack.append(int(token))

        else:
            v1=stack.pop()
            v2=stack.pop()

            if token == "+":
                stack.append((v1+v2))

            elif token == "-":
                stack.append((v2-v1))

            elif token == "*":
                stack.append((v1*v2))

            else:
                stack.append(int(float(v2)/float(v1)))

    return stack.pop()