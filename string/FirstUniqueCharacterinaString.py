# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.

def firstUniqChar(s):
    count={}
    for char in s:
        count[char]=count.get(char,0)+1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1