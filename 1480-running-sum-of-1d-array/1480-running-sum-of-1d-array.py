class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Start from the second element (index 1)
        for i in range(1, len(nums)):
            # Add the value of the previous index to the current index
            nums[i] += nums[i - 1]
        return nums