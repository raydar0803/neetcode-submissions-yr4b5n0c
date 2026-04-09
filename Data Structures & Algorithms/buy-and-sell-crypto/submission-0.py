class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two-pointer technique
        maxProfit = 0
        l, r = 0, 1 # left = buy, right = sell
        while(r < len(prices)):
            if(prices[l] < prices[r]):
                #profitable
                profit = prices[r] - prices [l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r += 1
        return maxProfit



        
        