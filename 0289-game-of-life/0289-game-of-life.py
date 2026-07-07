class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                lives = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        if (x, y) != (i, j):
                            lives += board[x][y] & 1
                
                if board[i][j] == 1 and (lives == 2 or lives == 3):
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
                    
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1