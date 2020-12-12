def checkPerfectNumber(num):
    res=[]
    ans,sqrt=0,int(num**0.5)
    if num <= 0: return False

    for i in range(1,sqrt+1):
        if num%i==0:
            ans+=i+num//i
    if num == sqrt ** 2: ans -= sqrt
    return ans - num == num
