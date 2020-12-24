def titleToNumber(self, s: str) -> int:
    s=s[::-1]
    ans=0

    for exp, char in enumerate(s):
        ans+=(ord(char)- 65 +1) * 26**exp
    return ans