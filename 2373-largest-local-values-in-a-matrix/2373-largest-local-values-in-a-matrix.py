class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # Initialize the result matrix of size (n-2) x (n-2)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        
        # Iterate over each 3x3 window's top-left corner
        for i in range(n - 2):
            for j in range(n - 2):
                # Find the maximum in the 3x3 window starting at grid[i][j]
                max_val = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        max_val = max(max_val, grid[r][c])
                
                # Assign the maximum value to the result matrix
                res[i][j] = max_val
                
        return res