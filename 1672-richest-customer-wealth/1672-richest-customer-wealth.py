class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for customer in accounts:
            # Calculate the sum of the current customer's accounts
            current_wealth = sum(customer)
            
            # Update max_wealth if the current customer's wealth is higher
            if current_wealth > max_wealth:
                max_wealth = current_wealth
                
        return max_wealth