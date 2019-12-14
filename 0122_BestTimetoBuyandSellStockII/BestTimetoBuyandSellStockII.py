class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(len(prices)-1):
            ret += max(0, prices[i+1] - prices[i])
        return ret

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret, cur_profit, cur_lo = 0, 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[cur_lo]: cur_lo = i
            old_profit = cur_profit
            cur_profit = max(cur_profit, prices[i] - prices[cur_lo])
            # check if profit still increasing
            if old_profit != cur_profit:
                ret += cur_profit
                cur_lo, cur_profit = i, 0
        return ret