class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                c+=1
            else:
                c=0
            m=max(m,c)
        return m