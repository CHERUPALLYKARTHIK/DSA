class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable_indices = []
        
        # Start from index 1 as mountain 0 has no preceding mountain
        for i in range(1, len(height)):
            # Check if the previous mountain's height is strictly greater than the threshold
            if height[i - 1] > threshold:
                stable_indices.append(i)
                
        return stable_indices