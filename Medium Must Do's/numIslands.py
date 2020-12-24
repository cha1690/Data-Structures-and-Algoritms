def numIslands(matrix):
    count=0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]== '1':
                dfs(matrix,i,j)
                count+=1
    return count

def dfs(grid,i,j):
    if i<0 or i>=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] !='1':
        return
    grid[i][j]='#'
    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j-1)
    dfs(grid,i,j+1)