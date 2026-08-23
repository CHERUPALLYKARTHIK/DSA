class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_left = sum(int(c) for c in num[:half] if c.isdigit())
        sum_right = sum(int(c) for c in num[half:] if c.isdigit())
        
        q_left = sum(1 for c in num[:half] if c == '?')
        q_right = sum(1 for c in num[half:] if c == '?')
        
        # Correct check: use *4.5 instead of //2*9
        return (sum_left - sum_right) != (q_right - q_left) * 9 / 2
