class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        results = []
        
        for q in queries:
            idx = P.index(q)
            results.append(idx)
            P.pop(idx)
            P.insert(0, q)
            
        return results