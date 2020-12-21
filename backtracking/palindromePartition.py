def palindromeParti(string):
    res=[]
    def backtrack(palin,s):
        if not s:
            res.append(palin)
            return
        else:
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    backtrack(palin + [s[:i]],s[i:])
    backtrack()
    return res