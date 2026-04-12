
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True 
    
    def search_words(self, r, c, board):
        row, col = len(board), len(board[0])
        words = []
        visit = set()

        def dfs(r, c, board, word, curr_node, prev):
            if min(r, c) < 0 or (r, c) in visit or r >= row or c >= col:
                return
            curr_letter = board[r][c]

            if curr_letter not in curr_node.children:
                return 
            
            word += curr_letter 
            visit.add((r, c))
            curr_node = curr_node.children[curr_letter]

            if curr_node.word:
                words.append(word)
            if (r + 1, c) != prev:
                dfs(r + 1, c, board, word, curr_node, (r, c))
            if (r - 1, c) != prev:
                dfs(r - 1, c, board, word, curr_node, (r, c))
            if (r, c + 1) != prev:
                dfs(r, c + 1, board, word, curr_node, (r, c))
            if (r, c - 1) != prev:
                dfs(r, c - 1, board, word, curr_node, (r, c))

            visit.remove((r, c))
        
        dfs(r, c, board, '', self.head, None)
        return words
            

                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        word_tree = Trie()
        for word in words:
            word_tree.insert(word)
        
        row, col = len(board), len(board[0])
        
        for r in range(row):
            for c in range(col):
                matching_words = word_tree.search_words(r, c, board)
                res += matching_words
        
        return list(set(res))



    