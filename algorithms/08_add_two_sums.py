class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def mult_two_digits(d1, d2, c):
            """
                mutiply two digits and an int, returns the result
                eg. "3", "9", 5--> "9", "2"
            """
            sum = int(d1) * int(d2) + c
            return str(sum%10), sum//10
            
        def add_two_digits(d1, d2, c):
            """
                multiply two digits and an int, returns the result
                eg. "3", "9", 5 --> "7", "1"
            """
            sum = int(d1) + int(d2) + c
            return str(sum%10), sum//10
            
            
        def mult_digit(digit1, digit2, move):
            """
                add a single char and a str and an int and return an array of chars
                eg. "204", "1", "0" --> 204
                    "204", "1", "3" --> 204000
            """
            if digit2 == "0":
                return "0"
                
                
            d_i = 1
            sum = []
            carry = 0
            while d_i - 1 < len(digit1):
                new_digit, carry = mult_two_digits(digit1[-d_i], digit2, carry)
                sum.insert(0, new_digit)
                d_i += 1

            # if there's a carry, append that to beginning of array
            if carry > 0:
                sum.insert(0, str(carry))
                
            return sum + ["0"] * move
            
            
        def add_two_nums(sums, to_add):
            """
                add two nums together
                input: two arrays
                output: one array
                eg. ["1", "2", "3], ["4", "5", "0"] --> ["5", "7", "3"]
                note: we can assume here that length of to_add is equal or more than length of sums
            """
            if len(sums) == 0:
                return to_add
                
            if to_add == "0":
                return sums
        
            d_i = 1
            diff = len(to_add) - len(sums)
            sum_arr = []
            carry = 0
            
            while d_i - 1 < len (sums):
                new_digit, carry = add_two_digits(sums[-d_i], to_add[-d_i], carry)
                sum_arr.insert(0, new_digit)
                d_i += 1
                
            while d_i -1 < len(to_add):
                new_digit, carry = add_two_digits("0", to_add[-d_i], carry)
                d_i += 1
                sum_arr.insert(0, new_digit)
                
                
            if carry > 0:
                sum_arr.insert(0, str(carry))
                
            return sum_arr
            
        if num1 == "0" or num2 == "0":
            return "0"
            
            
        move = 0
        sum_arr = []
        while move < len(num2):
            new_line = mult_digit(num1, num2[-move-1], move)
            sum_arr = add_two_nums(sum_arr, new_line)
            move += 1
            
        return "".join(sum_arr)