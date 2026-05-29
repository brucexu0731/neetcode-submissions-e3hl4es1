class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])
        def dfs(i, j, n, visit):
            if n == len(word):
                return True
                
            if (i == row or j == col or min(i, j) < 0 or board[i][j] != word[n] 
            or (i, j) in visit):
                return False
            
            visit.add((i, j))
            top = dfs(i - 1, j, n + 1, visit)
            down = dfs(i + 1, j, n + 1, visit)
            left = dfs(i, j - 1, n + 1, visit)
            right = dfs(i, j + 1, n + 1, visit)
            visit.remove((i, j))
            return top or down or left or right
        
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0, set()):
                    return True
        
        return False