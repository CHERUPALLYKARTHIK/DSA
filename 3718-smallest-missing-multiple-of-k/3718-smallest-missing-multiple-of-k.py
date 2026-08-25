class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ns= set(nums)   # Fast lookup
        m = k
        while m in ns:
            m += k
        return m
        