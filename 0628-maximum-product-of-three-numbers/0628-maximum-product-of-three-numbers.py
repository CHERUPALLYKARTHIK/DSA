class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a=sorted(nums,reverse=True)
        return max(a[0]*a[1]*a[2],a[0]*a[-1]*a[-2])

        