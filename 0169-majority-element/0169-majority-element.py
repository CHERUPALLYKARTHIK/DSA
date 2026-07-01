class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        '''dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        ans=-1
        temp=n//2
        for i in dici:
            val=dici[i]
            if val>temp:
                ans=i
                break 
        return ans'''
        c=0
        el=0
        for i in range(n):
            if c==0:
                c=1
                el=nums[i]
            elif el==nums[i]:
                c+=1
            else:
                c-=1
        cnt1 = nums.count(el)
        if cnt1 > (n // 2):
            return el
        return -1




        