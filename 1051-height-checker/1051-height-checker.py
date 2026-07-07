class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        c=0
        n=len(heights)
        for i in range(n):
            if heights[i]!=expected[i]:
                c+=1
        return c
        

        