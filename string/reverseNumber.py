def reverseNum(x):
    if x<0:
        return False
    num=abs(x)
    reverser_number=0
    while num:
        reverser_number=reverser_number*10+num%10
        num//=10
    if reverse_num==x:
        return True
    else: return False