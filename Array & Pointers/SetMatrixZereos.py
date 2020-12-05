class Solution:
    def setZeroes(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        col_zero = False
        row_zero = False

        for i in range(rows):
            if matrix[i][0] == 0:
                row_zero = True

        for j in range(cols):
            if matrix[0][j] == 0:
                col_zero = True

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    matrix[0][col]=0
                    matrix[row][0]=0

        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][0] == 0 or matrix[0][col] ==0:
                    matrix[row][col]=0

        if col_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if row_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0




