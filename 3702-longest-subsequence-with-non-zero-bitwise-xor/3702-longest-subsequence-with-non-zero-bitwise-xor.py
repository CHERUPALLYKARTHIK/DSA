class Solution:
    def longestSubsequence(self, numbers: List[int]) -> int:
        x = 0
        nz = False

        for num in numbers:
            x ^= num
            if num != 0:
                nz= True

        if x != 0:
            return len(numbers)

        if nz:
            return len(numbers) - 1

        return 0