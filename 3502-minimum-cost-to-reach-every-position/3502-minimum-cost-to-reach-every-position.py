class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        answer = [0] * n
        current_min = cost[0]
        
        for i in range(n):
            if cost[i] < current_min:
                current_min = cost[i]
            answer[i] = current_min
            
        return answer