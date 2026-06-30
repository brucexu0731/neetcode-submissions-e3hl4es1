class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = set()
        cols = set()

        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            for j in range(col):
                matrix[i][j] = 0
        
        for i in range(row):
            for j in cols:
                matrix[i][j] = 0
        