class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''a=min(nums)
        return a'''
        n=len(nums)
        l=0
        h=n-1
        ans=float(inf)
        while l<=h:
            m=(l+h)//2
            if nums[l]<=nums[m]:
                ans=min(ans,nums[l])
                l=m+1
            else:
                ans=min(ans,nums[m])
                h=m-1
        return ans
        