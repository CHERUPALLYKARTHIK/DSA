class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        '''a=[]
        a1=max(nums1)
        a2=max(nums2)
        a.append(a1)
        a.append(a2)
        n=len(a)
        i=0
        j=n-1
        if a[i]<a[j]:
            x=a[j]-a[i]
        elif a[i]>a[j]:
            x=a[j]-a[i]
        else:
            x=0
        return x'''
        return max(nums2)-max(nums1)        