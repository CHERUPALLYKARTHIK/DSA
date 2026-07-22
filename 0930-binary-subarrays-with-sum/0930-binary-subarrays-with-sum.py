class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        def fun(nums,k):
            l=0
            temp=0
            ans=0
            if k<0:
                return 0
            for r in range(len(nums)):
                if nums[r]==1:
                    temp+=1
                while temp>k:
                    if nums[l]==1:
                        temp-=1
                    l+=1
                ans+=r-l+1
            return ans
        return fun(nums,k)-fun(nums,k-1)
        

        