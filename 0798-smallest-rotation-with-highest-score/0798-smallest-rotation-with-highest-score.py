class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        # diff[k] will store the change in score at rotation k
        diff = [0] * n
        
        for i, val in enumerate(nums):
            # l is the first rotation where nums[i] begins to earn a point
            # r is the first rotation where nums[i] stops earning a point
            l = (i + 1) % n
            r = (n + i + 1 - val) % n
            
            # Apply the difference updates
            diff[l] += 1
            diff[r] -= 1
            
            # If the interval wraps around (l >= r), it means the element
            # earns a point at rotation 0, so we adjust the diff array accordingly
            if l >= r:
                diff[0] += 1
                
        # Use prefix sums to calculate the total score for each rotation
        max_score = -1
        best_k = 0
        current_score = 0
        
        for k in range(n):
            current_score += diff[k]
            if current_score > max_score:
                max_score = current_score
                best_k = k
                
        return best_k