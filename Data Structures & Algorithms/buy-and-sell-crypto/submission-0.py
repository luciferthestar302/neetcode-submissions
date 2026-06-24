class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Brute force code written by me
        n = len(prices)
        profit, profit_max = 0,0
        for i in range(0,n):
            for j in range(i+1,n):
                profit = prices[j]-prices[i]
                if profit>0:
                    profit_max = max(profit_max, profit) 
        return profit_max
        