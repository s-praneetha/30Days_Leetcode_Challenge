class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 2 or len(board[0]) < 2:
            return
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                self.dfs(board, i, len(board[0]) - 1)
                
        for j in range(1, len(board[0])):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[len(board) - 1][j] == 'O':
                self.dfs(board, len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                    
    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = 'B'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)