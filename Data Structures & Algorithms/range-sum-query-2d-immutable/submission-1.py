class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):
            row = []
            row_tot = 0
            tot = 0
            for j in range(len(matrix[0])):
                row_tot += matrix[i][j]
                tot = row_tot if i == 0 else row_tot + self.prefix[i - 1][j]
                row.append(tot)
            self.prefix.append(row)
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return (self.prefix[row2][col2] - self.prefix[row1 - 1][col2] - 
            self.prefix[row2][col1 - 1] + self.prefix[row1 - 1][col1 - 1])
        elif row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        elif row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1 - 1]
        elif col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1 - 1][col2]
        else: 
            return 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)