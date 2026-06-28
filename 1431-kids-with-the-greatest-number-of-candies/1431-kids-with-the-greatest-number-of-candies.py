class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Find the current maximum number of candies
        max_candies = max(candies)
        
        # Step 2: Compare each kid's potential total with the max
        # and create the boolean result list
        return [candy + extraCandies >= max_candies for candy in candies]