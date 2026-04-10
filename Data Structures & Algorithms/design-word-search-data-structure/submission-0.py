class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False 


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True 

    def search(self, word: str) -> bool:
        print(self.head.children.keys())
        
        def dfs(head, word):
            if len(word) == 0:
                return head.word 
            
            if word[0] == '.':
                for key in head.children:
                    if dfs(head.children[key], word[1:] if len(word) > 0 else ''):
                        return True 
                return False 
            elif word[0] not in head.children:
                return False
            else:
                return dfs(head.children[word[0]], word[1:] if len(word) > 0 else '')
        
        return dfs(self.head, word)
