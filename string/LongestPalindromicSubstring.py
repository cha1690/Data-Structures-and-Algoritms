def longeststring(s):
    m=''
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if len(m) >= j-i:
                continue
            if s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                continue
    return m