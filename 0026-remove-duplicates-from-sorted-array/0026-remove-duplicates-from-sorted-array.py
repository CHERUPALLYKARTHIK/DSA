class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        i=0
        nums[i]=nums[0]
        for j in range(n):
            if nums[i]==nums[j]:
                continue
            else:
                i=i+1
                nums[i]=nums[j]
        return i+1            

