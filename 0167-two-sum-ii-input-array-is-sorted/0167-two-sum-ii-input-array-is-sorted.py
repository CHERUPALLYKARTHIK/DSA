class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        while l<r:
            s=nums[l]+nums[r]
            if s==t:
                return [l+1,r+1]
            elif s<t:
                l+=1
            else:
                r-=1
        return [-1,-1]
        