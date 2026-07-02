class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_hourglass_sum = 0
        
        # Iterate through all possible top-left corners of a 3x3 block
        for i in range(m - 2):
            for j in range(n - 2):
                # Calculate the sum of the current hourglass
                current_sum = (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                    grid[i+1][j+1] +
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                )
                
                # Update the maximum sum found so far
                if current_sum > max_hourglass_sum:
                    max_hourglass_sum = current_sum
                    
        return max_hourglass_sum