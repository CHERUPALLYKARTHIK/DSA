class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        # Step 1: Collect elements into diagonals
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        
        # Step 2: Sort each diagonal in descending order for easy popping
        for key in diagonals:
            diagonals[key].sort(reverse=True)
            
        # Step 3: Replace elements in the matrix
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
                
        return mat