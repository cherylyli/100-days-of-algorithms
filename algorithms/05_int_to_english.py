# Notes: could definitely be optimized better
#
#
#
#
#


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        digits_to_str = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens_to_str = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        larger_to_str = ["Trillion", "Billion", "Million", "Thousand"]
        
        
        output_strs_by_hundred = []
        working_num = num
        pass_num = 0
        while working_num > 0:
            pass_num += 1
            temp_num = working_num%1000
            working_num = int(working_num/1000)
            
            tens = temp_num % 100
            hundred = int(temp_num / 100)
            if tens == 0:
                output_str = ""
            elif tens > 0 and tens <20:
                output_str = digits_to_str[tens] + ""
            else:
                output_str = tens_to_str[int(tens/10 - 2)] +" " + digits_to_str[tens%10]
                
            output_str = output_str.strip()
                
            if hundred > 0:
                output_str = digits_to_str[hundred] + " Hundred " + output_str
            output_str = output_str.strip()
            
            print("output: " + output_str)
            output_strs_by_hundred.insert(0,output_str)
        
        output = output_strs_by_hundred[0]
        output_strs_by_hundred = output_strs_by_hundred[1:]

        how_many_thousand = pass_num - 1
        larger_to_str = larger_to_str[len(larger_to_str)-how_many_thousand:]
        for i in range(0, how_many_thousand):
            if len(output_strs_by_hundred[0]) > 0:
                output += " " + larger_to_str[i] + " " + output_strs_by_hundred[0]
            else:
                output += " " + larger_to_str[i]
            output_strs_by_hundred = output_strs_by_hundred[1:]
            
        # if there's a 'million' and 'thousand' next to each other, or 'million' and 'billion', or 'billion' and 'trillion'
        # then strip the smaller one
        output_check = output.strip().split(" ")
        i = 1
        while i < len(output_check):
            if output_check[i-1] in larger_to_str and output_check[i] in larger_to_str:
                del output_check[i]
            else:
                i += 1
                
        return " ".join(output_check)
            
        