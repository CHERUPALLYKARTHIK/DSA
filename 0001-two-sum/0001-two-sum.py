class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        '''for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]'''
        s=[]
        #list
        for i,num in enumerate(nums):
            s.append((num,i))
        #sort
        s.sort(key=lambda x:x[0])
        l=0
        r=n-1
        while l<r:
            c_sum=s[l][0]+s[r][0]
            if c_sum==target:
                return s[l][1],s[r][1]
            elif c_sum<target:
                l+=1
            else:
                r-=1
        return [-1,-1]    
        

        