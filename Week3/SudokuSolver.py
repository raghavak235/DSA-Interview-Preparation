
https://leetcode.com/problems/sudoku-solver/
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def solve(board):
            for r in range(len(board)):
                for col in range(len(board[0])):
                    if board[r][col]=='.':
                        for c in '123456789':
                            if isvalid(board, r, col, c):
                                board[r][col]=c

                                if(solve(board)):
                                    return True
                                else:
                                    #backtracking
                                    board[r][col]='.'

                        return False
                
            return True
    
        def isvalid(board, row, col, c):
            for i in range(9):

                # Verifying Rows
                if board[i][ col]==c:
                    return False
                # Verifying Columns
                if board[row][i]==c:
                    return False
                
                # Veriying 3 * 3 matrix
                # Row Index: 33*(row//3)+i//3
                # Column Index:  3*(col//3)+i%3
                if(board[3*(row//3)+i//3][3*(col//3)+i%3] == c):
                        return False
            return True

        solve(board)
        
        

        
