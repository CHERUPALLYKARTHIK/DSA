class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        d=-1
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    temp=nums[j]-nums[i]
                    d=max(temp,d)
        return d