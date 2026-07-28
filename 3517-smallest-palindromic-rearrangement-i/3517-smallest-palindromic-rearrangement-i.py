class Solution:

    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        # Sort the first half to make it lexicographically smallest
        left = "".join(sorted(s[: n // 2]))

        # Get the middle character if the string length is odd
        mid = s[n // 2] if n % 2 == 1 else ""

        # Mirror the left half to complete the palindrome
        return left + mid + left[::-1]