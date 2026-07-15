class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        n=len(nums)
        def fo(nums,n,t):
            n=len(nums)
            l=0
            h=n-1
            f=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==t:
                    f=m
                    h=m-1
                elif nums[m]<t:
                    l=m+1
                else:
                    h=m-1
            return f
        def lo(nums,n,t):
            n=len(nums)
            l=0
            h=n-1
            l=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==t:
                    l=m
                    l=m+1
                elif nums[m]<t:
                    l=m+1
                else:
                    h=m-1
            return l
        f=fo(nums,n,t)
        if f==-1:
            return [-1,-1]
        l=lo(nums,n,t)
        return [f,l-1]

        
        