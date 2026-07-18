class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        gcd=1
        for i in range(1,a+1):
            if a%i==0:
                if b%i==0:
                    if i>gcd:
                        gcd=i
        return gcd               


        
        