class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def func(nums,k):
            n=len(nums)
            l=0
            dici={}
            ans=0
            for r in range(n):
                val=nums[r]
                if val in dici:
                    dici[val]+=1
                else:
                    dici[val]=1
                while len(dici)>k:
                    lval=nums[l]
                    dici[lval]-=1
                    if dici[lval]==0:
                        dici.pop(lval)
                    l+=1
                ans+=r-l+1
            return ans
        return func(nums,k)-func(nums,k-1)
        