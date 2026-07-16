class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        n=len(a)
        if n==1:
            return a[0]
        if a[0]!=a[1]:
            return a[0]
        if a[n-1]!=a[n-2]:
            return a[n-1]
        l=1
        h=n-1
        while l<=h:
            m=(l+h)//2
            if a[m]!=a[m-1] and a[m]!=a[m+1]:
                return a[m] 
            if m%2==0 and a[m]==a[m+1] or m%2==1 and a[m]==a[m-1]:
                l=m+1
            else:
                h=m-1
        return -1       