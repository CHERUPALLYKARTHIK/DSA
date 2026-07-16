class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ''''l=len(nums)
        for i in range(l):
            if (i==0 or nums[i]>=nums[i-1]) and (i==l-1 or nums[i]>=nums[i+1]):
                return i
        return -1'''
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        l=1
        h=n-2
        while l<=h:
            m=(l+h)//2
            if nums[m]>nums[m-1] and nums[m]>nums[m+1]:
                return m
            elif nums[m]>nums[m-1]:
                l=m+1
            else:
                h=m-1
        return -1

        
        