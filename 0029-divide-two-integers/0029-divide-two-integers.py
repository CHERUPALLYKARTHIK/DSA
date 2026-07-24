class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1  # 2147483647
        MIN_INT = -2**31     # -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0

        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                quotient += 1 << i
                dividend -= divisor << i
                
        return -quotient if negative else quotient