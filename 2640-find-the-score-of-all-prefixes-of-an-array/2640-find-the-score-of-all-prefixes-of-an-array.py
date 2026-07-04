class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        cur=0
        run=0
        ans=[]
        for i in range(len(nums)):
            cur=max(cur,nums[i])
            val=nums[i]+cur
            run+=val
            ans.append(run)

        return ans

        