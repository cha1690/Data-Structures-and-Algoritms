def uniquePaths(m,n):

    dp = [[1]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]