class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_p = 0

        for p in prices:
            if p < min_price:
                min_price = p 
            max_p = max(max_p, p - min_price)
        
        return max_p 