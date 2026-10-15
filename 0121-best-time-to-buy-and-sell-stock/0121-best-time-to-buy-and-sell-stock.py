class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if buy_price> prices[i]:
                buy_price=prices[i]
            profit=max(profit,prices[i]-buy_price)
        return profit

    # class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     buyPrice=prices[0]
    #     profit=0
    #     for i in range(1,len(prices)):
    #         if buyPrice>prices[i]:
    #             buyPrice=prices[i]
    #         else:
    #             profit=max(profit,prices[i]-buyPrice)
    #     return profit
        