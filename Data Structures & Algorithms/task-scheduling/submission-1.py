from collections import defaultdict 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # i have a bunch of tasks consisting of 26 tasks, and the same task 
        # need to have a cooldown of n
        # so to minimize, I would need to ideally want to be able to fit each
        # task at least n spaces apart 

        # {X: 2, Y: 2} 
        # pick X, X now on cooldown for 2 turns 
        # pick Y, Y on cooldown for 2 turns, X on cooldown for 1 turn
        # use a hashmap to store all the letters on cooldown

        # each turn, we need to iterate through all the letters, find one that
        # is not on cooldown, add to the list, then update all cooldown values
        # -> constant time since only 26 letters 

        letters = defaultdict(int)
        cooldown = {}
        res = 0

        for c in tasks:
            letters[c] += 1
        
        while letters:
            print(letters)
            curr = ''
            #add a fresh letter, then add the letter to cooldown
            max_count = 0
            for c in letters:               
                if c not in cooldown and (letters[c] >= max_count):
                    max_count = letters[c]
                    curr = c
            if curr:
                letters[curr] -= 1
                cooldown[curr] = n 
            
            #if letter used up, pop it from letters
            if letters[curr] == 0:
                letters.pop(curr)
            
            #reduce buffer time by 1, if any letter is refreshed, remove from cooldown 
            refresh = []
            for c in cooldown:
                if c == curr:
                    continue
                cooldown[c] -= 1
                if cooldown[c] == 0:
                    refresh.append(c)
            
            for c in refresh:
                cooldown.pop(c)
            
            res += 1
        
        return res
            




