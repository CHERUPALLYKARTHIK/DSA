class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n=len(customers)
        t=0
        ct=0
        for arrival,time in customers:
            if ct<arrival:
                ct=arrival
            ct+=time
            t+=(ct-arrival)
        return t/n
        