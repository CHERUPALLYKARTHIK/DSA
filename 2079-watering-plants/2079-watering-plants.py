class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        
        for i, water_needed in enumerate(plants):
            # If we don't have enough water for the next plant
            if current_water < water_needed:
                # Walk back to the river (i steps) and back to the current plant (i steps)
                steps += (i * 2)
                current_water = capacity
            
            # Water the plant (1 step forward)
            current_water -= water_needed
            steps += 1
            
        return steps