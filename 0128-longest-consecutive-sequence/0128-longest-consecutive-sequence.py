class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        cnt=0
        l=0
        for x in num_set:
            if x-1 not in num_set:
                cnt=1
                cur=x
                while cur+1 in num_set:
                    cur+=1
                    cnt+=1
            l=max(l,cnt)
        return l 
        