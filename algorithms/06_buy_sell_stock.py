# Got distracted by previous stock question and attempted a suboptimal solution. 
# Then went to eat dinner and got a fresh perspective and solved in 15-20 min

# solution is O(n) where n is length of input array 


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # base case
        if len(prices) <= 1:
            return 0
            
        # go through list once
        max_dif = 0
        min = prices[0]
        max = prices[0]
        
        i = 1
        while i < len(prices):

            if prices[i] < min:
                # if current dif is larger than max_dif, then update max_dif, else update min = price & max = price
                if max - min > max_dif:
                    max_dif = max-min
                min = prices[i]
                max = prices[i]
                
            # price > max
            if prices[i] > max: 
                max = prices[i]
            i += 1
                
        if max-min > max_dif:
            return max-min
        return max_dif
            