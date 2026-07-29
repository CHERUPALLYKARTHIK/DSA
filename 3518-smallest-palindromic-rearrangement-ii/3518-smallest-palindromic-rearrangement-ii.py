import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        cnt = Counter(s)
        
        mid_char = ""
        half_cnt = {}
        for ch in sorted(cnt.keys()):
            c = cnt[ch]
            if c % 2 == 1:
                mid_char = ch
            half_cnt[ch] = c // 2
            
        def get_perms(freqs, limit):
            ans = 1
            running_sum = 0
            for f in freqs:
                if f == 0:
                    continue
                running_sum += f
                ans *= math.comb(running_sum, f)
                if ans >= limit:
                    return limit
            return ans

        # Check if total possible palindromes is at least k
        total_perms = get_perms(list(half_cnt.values()), k)
        if total_perms < k:
            return ""

        half_len = n // 2
        res = []

        # Construct the first half character by character
        for _ in range(half_len):
            for ch in sorted(half_cnt.keys()):
                if half_cnt[ch] == 0:
                    continue
                
                # Try placing character `ch` at current position
                half_cnt[ch] -= 1
                perms = get_perms(list(half_cnt.values()), k)
                
                if k <= perms:
                    res.append(ch)
                    break
                else:
                    k -= perms
                    half_cnt[ch] += 1

        first_half = "".join(res)
        return first_half + mid_char + first_half[::-1]