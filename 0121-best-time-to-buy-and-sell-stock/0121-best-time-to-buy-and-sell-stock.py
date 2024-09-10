class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_day_to_buy:int = prices[0]
        best_day_to_sell:int = prices[0]
        
        profit:int = 0
        
        for price in prices:
            if price < best_day_to_buy:
                best_day_to_buy = price
                best_day_to_sell = price
            elif price > best_day_to_sell:
                best_day_to_sell = price
                
                profit = max((best_day_to_sell - best_day_to_buy), profit)
                # if best_day_to_sell > best_day_to_buy:
                #     res =  best_day_to_sell - best_day_to_buy 
                #     if profit < res:
                #         profit = res
        
        return profit
                