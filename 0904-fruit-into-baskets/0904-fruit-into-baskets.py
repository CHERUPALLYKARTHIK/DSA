class Solution:
    def totalFruit(self, f: List[int]) -> int:
        n=len(f)
        l=0
        ans=0
        dici={}
        k=2
        for r in range(n):
            val=f[r]
            if val in dici:
                dici[val]+=1
            else:
                dici[val]=1
            while len(dici)>k:
                lval=f[l]
                dici[lval]-=1
                if dici[lval]==0:
                    dici.pop(lval)
                l+=1
            ans=max(ans,r-l+1)
        return ans
        