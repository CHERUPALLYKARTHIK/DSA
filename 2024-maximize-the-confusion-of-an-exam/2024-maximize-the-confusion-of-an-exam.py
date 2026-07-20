class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        n=len(a)
        cntt=0
        cntf=0
        l=0
        ans=0
        for r in range(n):
            if a[r]=='T':
                cntt+=1
            else:
                cntf+=1
            while min(cntt,cntf)>k:
                if a[l]=='F':
                    cntf-=1
                else:
                    cntt-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
        