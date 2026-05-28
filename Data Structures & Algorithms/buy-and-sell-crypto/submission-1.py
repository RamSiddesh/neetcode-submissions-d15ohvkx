class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lptr=0
        rptr=1
        maxProfit = 0
        while rptr < len(prices):
            if prices[lptr]>prices[rptr]:
                lptr = rptr
            else:
                if prices[rptr]-prices[lptr] > maxProfit:
                    maxProfit = prices[rptr]-prices[lptr]
                rptr+=1
        return maxProfit

