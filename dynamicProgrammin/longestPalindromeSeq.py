def longest(s):
    res=''
    for i in range(len(s)):
        res= max(helper(s,i,i),helper(s,i,i+1),res, key=len)

    return res

def helper(s,l,r):
    while l>=0 and r<len(s) and s[l]==s[r]:
        l+=1
        r-=1
    return s[l+1:r]