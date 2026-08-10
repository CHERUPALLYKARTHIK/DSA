class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        longest = ""
        for i in range(len(s)):
            # Odd length
            p1 = expand(i, i)
            # Even length
            p2 = expand(i, i+1)
            if len(p1) > len(longest): longest = p1
            if len(p2) > len(longest): longest = p2
        return longest

        