# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # #  Brute Force Approach.O(n2).O(1)
        total_profit=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit= prices[j]- prices[i]
                if profit > total_profit:
                    total_profit=profit
        print(total_profit)
        return total_profit

        # 2 Pointer Approach
        total_profit = 0
        i = 0
        j = 1
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit > total_profit:
                total_profit = profit
            elif prices[j] < prices[i]:
                i = j

            j += 1

        print(total_profit)
        return total_profit
