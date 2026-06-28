class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Calculate ones in each row and column
        onesRow = [sum(row) for row in grid]
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        # Build the difference matrix
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Using the simplified formula: 
                # diff[i][j] = 2 * (onesRow[i] + onesCol[j]) - m - n
                diff[i][j] = 2 * (onesRow[i] + onesCol[j]) - m - n
                
        return diff