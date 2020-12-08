# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


def countAndSay(n):
    start='1'
    for i in range(n):
        start= nextNumber(start)
    return start

def nextNumber(start):
    res=''
    freq=1
    for i in range(len(start)):
        if i+1<= len(start) and start[i]==start[i+1]:
            freq+=1
            continue
        else:
            res += str(freq)+start[i]
            freq=1
    return res