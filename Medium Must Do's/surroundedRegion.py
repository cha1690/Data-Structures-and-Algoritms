def supproundedRegion(matrix):
    # outside in approach
    # check all the corner cells and mark them.. convert the rest of the matrix '0' to 'X'

    queue= collections.deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i in [0, len(matrix)-1] or j in [0, len(matrix[0])-1]) and matrix[i][j]=='0':
                queue.append((i,j))

    while queue:
        r,c = queue.popleft()
        if 0<=r<len(matrix) and 0<=c<len(matrix[0]) and matrix[i][j]=='0':
            matrix[r][c]='.'
            queue.extend([(r-1,c),(r+1,c),(r,c-1),(r,c+1)])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                matrix[i][j] = 'X'
            if matrix[i][j] == '.':
                matrix[i][j] = '0'
