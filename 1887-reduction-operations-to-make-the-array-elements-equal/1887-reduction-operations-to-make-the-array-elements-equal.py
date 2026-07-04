class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        o=0
        r=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                r+=1
            o+=r
        return o
        