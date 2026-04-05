class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix) - 1

        while l1 <= r1:
            m = (l1 + r1) // 2
            if matrix[m][0] < target:
                l1 = m + 1
            elif matrix[m][0] > target:
                r1 = m - 1
            else: 
                return True
        
        l2 = 0
        r2 = len(matrix[0]) - 1
        print("r1", r1)
        while l2 <= r2:
            print("l2:", l2)
            print("r2:", r2)
            m2 = (l2 + r2) // 2
            print("m2", m2)
            if matrix[r1][m2] < target:
                l2 = m2 + 1
            elif matrix[r1][m2] > target:
                r2 = m2 - 1
            else: 
                return True
        
        return False
        