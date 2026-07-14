class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            # Create a row filled with 1s, with a length of i + 1
            row = [1] * (i + 1)
            
            # Each element (except the first and last) is the sum of
            # the two elements directly above it in the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(row)
            
        return triangle
        