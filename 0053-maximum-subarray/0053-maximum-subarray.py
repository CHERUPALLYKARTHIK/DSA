class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        '''s=[]
        for i in range(n):
            cs=0
            for j in range(i,n):
                cs+=nums[j]
                s.append(cs)
        return max(s)'''
        sum=0
        maxi=float(-inf)
        for i in range(n):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
        return maxi     