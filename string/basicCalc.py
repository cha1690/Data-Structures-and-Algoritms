def basicCalc(s):
    if not s:
        return 0
    stack,num, sign=[],0,'+'

    for i in range(len(s)):
        if s[i].isdigit():
            num=num*10+int(s[i])
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign =='+':
                stack.append(num)
            if sign =='-':
                stack.append(-num)
            if sign =='*':
                stack.append(stack.pop()*num)
            if sign =='/':
                tmp = stack.pop()
                if tmp//num < 0 and tmp%num != 0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            num=0
            sign=s[i]

    return sum(stack)