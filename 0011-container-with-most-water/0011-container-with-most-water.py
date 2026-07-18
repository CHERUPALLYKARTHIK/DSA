class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        l=0
        r=n-1
        area=0
        while l<r:
            hei=min(h[l],h[r])
            b=r-l
            curarea=hei*b
            area=max(area,curarea)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return area


        