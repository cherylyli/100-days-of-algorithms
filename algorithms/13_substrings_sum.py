import math
number = [int(n) for n in input().strip()]

sub_sum = 0
pass_num = 0

# for each pass, group pass_num number of inputs together
while pass_num < len(number):
    pass_num += 1
    
    for ind, digit in enumerate(number):
        digit_sum = 0 
        if ind < pass_num-1 and len(number) - ind +1 > pass_num:
            for i in range(ind+1):
                sub_sum += math.pow(10, pass_num - i-1)*digit
            
        elif ind < pass_num - 1 and len(number) - pass_num < ind:
            for i in range(len(number)-pass_num+1):
                sub_sum += math.pow(10, pass_num-ind-1+i)*digit
                
        elif len(number) - ind < pass_num:
            for i in range(len(number) - ind):
                sub_sum += math.pow(10, i)*digit
            
        else: 
            for i in range(pass_num):
                sub_sum += math.pow(10, i)*digit
        
print(int(sub_sum%(math.pow(10, 9)+7)))
    
    