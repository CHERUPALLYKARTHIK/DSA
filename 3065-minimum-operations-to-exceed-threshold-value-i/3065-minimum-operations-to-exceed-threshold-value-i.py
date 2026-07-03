class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            if k > nums[i]:
                c+=1
        return c

        