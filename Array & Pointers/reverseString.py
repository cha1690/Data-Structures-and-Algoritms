def reverseWords(self, s: str) -> str:
    l,r=0, len(s)-1
    while l<=r and s[l] == " ":
        l+=1

    while l<=r and s[r] == " ":
        r-=1

    d= collections.deque()
    word=[]

    while l<=r:
        if s[l] == ' ' and word:
            d.appendleft("".join(word))
            word=[]
        elif s[l] != " ":
            word.append(s[l])
        l+=1
    d.appendleft(''.join(word))

    return " ".join(d)