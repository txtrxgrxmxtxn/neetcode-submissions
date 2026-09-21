class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        if not prices or len(prices) < 2: 
            return 0

        
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:

            #update min price seen:
            min_price = min(min_price, price)
            #calculate the profit 
            profit = price - min_price

            #update max_profit 
            max_profit = max(max_profit, profit)


        return max_profit

