def generateParenthesis(self, n: int) -> List[str]:
    res=[]

    def backtrack(combi, left, right):
        if len(combi) == 2*n:
            res.append(combi)
            return
        if left < n:
            backtrack(combi+'(',left+1,right)
        if right<left:
            backtrack(combi+')',left, right+1)

    backtrack('',0,0)

    return res