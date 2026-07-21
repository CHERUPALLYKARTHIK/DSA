class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def f1(nums,k):
            l=0
            n=len(nums)
            ans=0
            temp=0
            for r in range(n):
                if nums[r]%2==1:
                    temp+=1
                while temp>k:
                    if nums[l]%2==1:
                        temp-=1
                    l+=1
                ans+=r-l+1
            return ans 
        return f1(nums,k)-f1(nums,k-1)

        