class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Step 1: Extract and sort only the x-coordinates
        x_coords = sorted([p[0] for p in points])
        
        max_width = 0
        
        # Step 2: Find the maximum gap between adjacent x-coordinates
        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i-1]
            if width > max_width:
                max_width = width
                
        return max_width
        