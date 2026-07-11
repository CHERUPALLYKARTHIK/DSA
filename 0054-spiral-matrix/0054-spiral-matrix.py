class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        res=[]
        rowb=0
        rowe=r-1
        colb=0
        cole=c-1
        while rowb<=rowe and colb<=cole:
            for j in range(colb,cole+1):
                res.append(matrix[rowb][j])
            rowb+=1

            for i in range(rowb,rowe+1):
                res.append(matrix[i][cole])
            cole-=1

            if rowb<=rowe:
                for j in range(cole,colb-1,-1):
                    res.append(matrix[rowe][j])
                rowe-=1
            
            if colb<=cole:
                for i in range(rowe,rowb-1,-1):
                    res.append(matrix[i][colb])
                colb+=1
        return res



        