def isValidSudoku(board) -> bool:
    seen = set()
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != '.':
                curr = board[row][col]
                if (curr, row) in seen or (col, curr) in seen or (row//3, col//3, curr) in seen:
                    return False
                seen.add((curr, row))
                seen.add((col, curr))
                seen.add((row//3, col//3, curr))
    return True