from collections import defaultdict
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #sort first
        # build frequency map
        #keep picking groups of size groupSize starting from the smallest
        #number until either we exhausted the whole list or we failed to build group
        # This works because a valid group of straights from any list would
        # guarantee to include its smallest element first, so we can prove by
        # induction

        freq = defaultdict(int)
        for num in hand:
            freq[num] += 1
        heapq.heapify(hand)
        
        size = len(hand)
        while size > 0:
            #print(size)
            if size < groupSize:
                return False
                
            curr = heapq.heappop(hand)
            size -= 1
            #print("curr", curr)
            #print("size", size)
            freq[curr] -= 1
            for i in range(1, groupSize):
                if curr + i not in freq or freq[curr + i] == 0:
                    return False 
                freq[curr + i] -= 1
                size -= 1
            print(hand)
            while hand and (hand[0] not in freq or freq[hand[0]] <= 0):
                heapq.heappop(hand)

        return True 
                
            

