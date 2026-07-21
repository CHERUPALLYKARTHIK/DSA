class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def func(dicia,dicib):
            if len(dicia)!=len(dicib):
                return False
            for i in dicia:
                if i not in dicib or dicia[i]!=dicib[i]:
                    return False
            return True
        dicia={}
        dicib={}
        l=0
        ans=[]
        n=len(s)
        k=len(p)
        for i in p:
            if i in dicib:
                dicib[i]+=1
            else:
                dicib[i]=1
        for r in range(n):
            val=s[r]
            if val in dicia:
                dicia[val]+=1
            else:
                dicia[val]=1
            if r-l==k:
                lval=s[l]
                dicia[lval]-=1
                if dicia[lval]==0:
                    dicia.pop(lval)
                l+=1
            if r-l+1==k:
                if func(dicia,dicib):
                    ans.append(l)
        return ans
        