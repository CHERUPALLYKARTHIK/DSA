class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # Create (m+1) x (n+1) prefix sum matrix initialized to 0
        P = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Precompute prefix sums
        for i in range(m):
            for j in range(n):
                P[i + 1][j + 1] = mat[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]
        
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Define boundaries for the block
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m, i + k + 1), min(n, j + k + 1)
                
                # Use inclusion-exclusion to get sum in O(1)
                ans[i][j] = P[r2][c2] - P[r1][c2] - P[r2][c1] + P[r1][c1]
        
        return ans