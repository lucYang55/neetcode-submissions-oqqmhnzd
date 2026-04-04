class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # but on the second day then sell on the 5 
        l = 0 
        r = 1
        profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r  
            else:
                profit = max(profit, prices[r] - prices[l])
            r += 1 
        
        return profit
                
