def letterCombinations(self, digits: str) -> List[str]:
    lettermapping = { '2':["a", "b", "c"], '3':["d","e","f"],
                      '4':["g","h","i"], '5':["j","k","l"],
                      '6':["m","n","o"], '7':["p","q","r","s"] ,
                      '8':["t","u","v"], '9':["x","w","y","z"] }
    res=[]

    def backtrack(combi, digits):
        if not digits:
            res.append(combi)
        else:
            for letter in lettermapping[digits[0]]:
                backtrack(combi+letter, digits[1:])

    if digits:
        backtrack("",digits)
    return res