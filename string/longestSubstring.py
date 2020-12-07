
def longestSubstring(s):
    seen={}
    startIndex=maxLength=0
    for index,char in enumerate(s):
        if char in seen and startIndex <= seen[char]:
            startIndex = index+1
        else:
            maxLength= max(maxLength, index-startIndex+1)
        seen[char] = index
    return maxLength