class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #Brute Force
        pos=[]
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
        return nums

        