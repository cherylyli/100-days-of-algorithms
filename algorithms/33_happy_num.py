class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calc_squares(n):
            """
            :type n: int
            :rtype: int
            given a 2 or more digits number, return the sum of the square roots of each digit
            """
            sum = 0
            while n>0:
                d = n%10
                n = n//10
                sum += d * d
            return sum
        
        
        # single digit numbers:
        # 0 and 1 - happy
        # 2-9 - not happy
        # base cases
        happy_or_nah = {0: True, 1: True, 2: False, 3: False, 4: False, 5:False, 6:False, 7:True, 8:False, 9:False}
        
        new_sum = n
        
        while new_sum not in happy_or_nah:
            new_sum = calc_squares(new_sum)
            
        return happy_or_nah[new_sum]
        