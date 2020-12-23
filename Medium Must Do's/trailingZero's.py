def trailingZeroes(self, n: int) -> int:
    count=0
    while n>0:
        n//=5
        print(n)
        count+=n
    return count