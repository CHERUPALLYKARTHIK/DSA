class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum value in each row
        row_minima = {min(row) for row in matrix}
        
        # Step 2: Find the maximum value in each column
        # zip(*matrix) transposes the matrix to make column iteration easy
        col_maxima = {max(col) for col in zip(*matrix)}
        
        # Step 3: Return the intersection of both sets
        # A lucky number must be both a row minimum and a column maximum
        return list(row_minima.intersection(col_maxima))