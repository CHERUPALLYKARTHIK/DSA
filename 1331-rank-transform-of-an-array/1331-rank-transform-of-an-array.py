class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(list(set(arr)))
        rank={}
        for i in range(len(a)):
            val=a[i]
            r=i+1
            rank[val]=r
        res=[]
        for x in arr:
            res.append(rank[x])
        return res
        