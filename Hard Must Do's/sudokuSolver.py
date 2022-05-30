
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
    
    def checkunassigned(self):
        row, col = -1, -1
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == ".":
                    row, col = r, c
        return row, col
    
    def solve(self):
        row, col = self.checkunassigned()
        if row ==-1 and col == -1:
            return True
        for num in ["1","2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.checkvalid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False
    
    def checkvalid(self, row, col, num):
        box_row = row - row%3
        box_col = col - col%3
        
        if self.checkrow(row, num) and self.checkcol(col, num) and self.checkbox(box_row, box_col, num):
            return True
        return False
    
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
       
    def checkbox(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True
        
        
