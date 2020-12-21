def wordSearch(matrix, word):
    rows=len(matrix)
    cols=len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if dfs(matrix, row, col, word):
                return True

    return False

def dfs(matrix, i, j, word):

    if len(word)==0:
        return True

    elif i<0 or i>len(matrix) or j<0 or j>len(matrix[0]) or matrix[i][j] != word[0]:
        return False

    tmp = board[i][j]
    board[i][j]= '#'

    res= dfs(matrix, i+1, j, word[1:]) or dfs(matrix, j+1, i, word[1:]) or dfs(matrix, i-1, j, word[1:]) or dfs(matrix, i, j-1, word[1:])

    board[i][j]= tmp

    return res