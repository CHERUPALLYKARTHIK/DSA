class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #Brute Force
        '''pos=[]
        neg=[]
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        if len(pos)==len(neg):
            for i in range(len(pos)):
                nums[2*i]=pos[i]
                nums[2*i+1]=neg[i]
        return nums'''
        #optimal solution
        n=len(nums)
        ans=[0]*n
        pos=0
        neg=1
        for i in range(n):
            if nums[i]<0:
                ans[neg]=nums[i]
                neg+=2
            else:
                ans[pos]=nums[i]
                pos+=2
        return ans


        