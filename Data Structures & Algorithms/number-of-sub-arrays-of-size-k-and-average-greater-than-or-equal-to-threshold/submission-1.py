class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        for l in range (len(arr) - k + 1):
            if sum(arr[l: l + k]) / k >= threshold:
                counter += 1
        
        return counter