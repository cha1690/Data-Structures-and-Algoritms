
def happyNumber(n):
    seen = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in seen:
            return False
        else:
            seen.add(n)
    return True

happyNumber(34)
