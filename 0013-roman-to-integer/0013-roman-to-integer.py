class Solution:
    def romanToInt(self, s: str) -> int:
        toRoman = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans = 0
        prev = 0

        for n in reversed(s):
            n = toRoman[n]

            if n < prev:
                ans -= n
            else:
                ans += n

            prev = n

        return ans
        