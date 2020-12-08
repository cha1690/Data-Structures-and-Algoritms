def isPalindrome(S):
    left,right=0, len(S)-1
    s = S.lower()
    seen='abcdefghijklmnopqrstuvwxyz'
    while left < right:
        if s[left] not in seen:
            left+=1
            continue
        if s[right] not in seen:
            right-=1
            continue
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

