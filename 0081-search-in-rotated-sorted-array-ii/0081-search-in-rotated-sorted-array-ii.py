class Solution:
    def search(self, nums: List[int], t: int) -> int:
        n=len(nums)
        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==t:
                return True
            if nums[l]==nums[m] and nums[m]==nums[h]:
                l+=1
                h-=1
                continue 
            if nums[l]<=nums[m]:
                if nums[l]<=t and t<=nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if nums[m]<=t and t<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return False 
        