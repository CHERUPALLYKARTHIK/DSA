class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniset=set()
        n=len(s)
        l=0
        ans=0
        for r in range(n):
            ch=s[r]
            if ch not in uniset:
                uniset.add(ch)
            else:
                while ch in uniset:
                    uniset.remove(s[l])
                    l+=1
                uniset.add(ch)
            ans=max(ans,r-l+1)
        return ans
        #Brute Force
        '''n=len(s)
        l=0
        for i in range(n):
            for j in range(i+1,n+1):
                sub=s[i:j]
                if len(set(sub))==len(sub):
                    l=max(l,j-i)
        return l'''
        