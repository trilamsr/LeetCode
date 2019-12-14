class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret, lo = 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[lo]: lo = i
            if i > lo: ret = max(ret, prices[i] - prices[lo])
        return ret

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret, lo = 0, float('inf')
        for price in prices:
            if price < lo: lo = price
            ret = max(ret, price - lo)
        return ret