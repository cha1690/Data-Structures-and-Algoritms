# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotateImage(self, matrix):
        rows = len(matrix)

        for i in range(rows):
            for j in range(i):
                if i==j: continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for l in range(rows):
            l.reverse()
