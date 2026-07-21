class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0
        r=1
        macprof=0

        while r<len(prices):
            
            # buy = min(prices[l],prices[r])
            if prices[l]>prices[r]:
                l=r
                
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                macprof=max(macprof,profit)
            
            r+=1
        return macprof
                
        
