from collections import defaultdict 
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for i in range(1, len(words)):
            w1, w2 = (words[i - 1]), words[i]
            is_prefix = True
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    is_prefix = False
                    break
            if is_prefix and len(w1) > len(w2):
                return ''
        chars = set()
        for word in words:
            for c in word:
                if c in chars:
                    continue
                chars.add(c)
                
        visit = set()
        res = []
        print(chars)


        def dfs(char, path):
            if char in path:
                return False
            if char in visit: 
                return True 

            if char not in adj:
                if char in chars:
                    chars.remove(char)
                    res.append(char)
                return True

            path.add(char)

            for nxt in adj[char]:
                if not dfs(nxt, path):
                    return False 
            
            visit.add(char)
            res.append(char)
            chars.remove(char)
            path.remove(char)
            return True

        print(adj)
        
        for key in list(adj.keys()):
            if not dfs(key, set()):
                return ''
        for c in chars:
            res.append(c)

        return ''.join(res[::-1])
            

            