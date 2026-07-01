class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        for i in range(n):
            if colors[i] != colors[n-1]:
                res = max(res, abs(i - (n-1)))
            if colors[i] != colors[0]:
                res = max(res, abs(i - 0))
        return res