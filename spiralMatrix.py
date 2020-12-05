# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


class Solution:
    def spiralOrder(self, matrix):

        res=[]
        top,bottom = 0, len(matrix)-1
        left, right= 0, len(matrix[0])-1

        while left <=right and top <=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            for j in range(top, bottom+1):
                res.append(matrix[j][right])
            right-=1

            if left > right or top > bottom:
                break

            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1

            for j in range(bottom,top-1,-1):
                res.append(matrix[j][left])
            left+=1

        return res