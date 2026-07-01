class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        rmax=-1
        for i in range(n-1,-1,-1):
            temp=arr[i]
            arr[i]=rmax
            rmax=max(rmax,temp)
        return arr
        '''#Brute force
        temp=0
        ans=[]
        for i in range(n-1):
            for j in range(i+1,n):
                temp=max(temp,arr[j])
            ans.append(temp)
        ans.append(-1)
        return ans'''


        