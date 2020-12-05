class Solution:
    def pascalsTriangle(self, numRows):
        res=[]
        for row in range(numRows):
            res.append([1]*(row+1))
            for col in range(1,row):
                res[row][col] = res[row-1][col] + res[row-1][col-1]

        return res