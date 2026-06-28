class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r, c = rStart, cStart
        # Directions: East, South, West, North
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        
        step = 1 # Number of steps to take in the current direction
        d = 0    # Current direction index
        
        while len(res) < rows * cols:
            # We move 'step' length twice before increasing 'step'
            for _ in range(2):
                for _ in range(step):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r += dr[d]
                    c += dc[d]
                # Turn right 90 degrees
                d = (d + 1) % 4
            # Increase step size after two turns
            step += 1
            
        return res