class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        '''for _ in range(n):
            rotated=[0]*n
        for i in range(n):
            for j in range(n):
                rotated[j][n-i-1]=matrix[i][j]
        return rotated'''
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix
        