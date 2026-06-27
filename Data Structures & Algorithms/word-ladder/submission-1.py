from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs? I start from beginning word and do bfs, edges are all reachable
        # words in word list until i get to the final word 

        def compare_words(w1, w2):
            diff_count = 1
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff_count -= 1
                if diff_count < 0:
                    return False
            return True

        queue = deque()
        wordList = set(wordList)
        depth = 1
        queue.append(beginWord)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return depth
                remove = []
                for w in wordList:
                    if compare_words(curr, w):
                        queue.append(w)
                        remove.append(w)
                for w in remove:
                    wordList.remove(w)
            depth += 1
        
        return 0





