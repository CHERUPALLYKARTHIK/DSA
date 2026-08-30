class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini=nums.index(min(nums))
        maxi=nums.index(max(nums))
        if mini>maxi:
            mini,maxi=maxi,mini
        f=maxi+1
        b=n-mini
        fb=(mini+1)+(n-maxi)
        ans=min(f,b,fb)
        return ans