class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        a=[0]
        m=0
        c=0
        for i in range(n):
            c+=gain[i]
            a.append(c)
        for i in range(len(a)):
            m=max(m,a[i])
        return m


        