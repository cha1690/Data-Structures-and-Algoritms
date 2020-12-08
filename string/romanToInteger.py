# Input: s = "III"
# Output: 3
# Input: s = "IV"
# Output: 4


def romanToInt(s):
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    ans=prev=0
    for i in s[::-1]:
        if roman[i] >= prev:
            ans+=roman[i]
        else:
            ans-=roman[i]
        prev= roman[i]
    return ans
