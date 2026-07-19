class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #sliding window
        nums.sort()
        l=0
        n=len(nums)
        ans=float('inf')
        for  r in range(n):
            if r-l==k:
                l+=1
            if r-l+1==k:
                m=nums[r]-nums[l]
                ans=min(ans,m)
        return ans
        