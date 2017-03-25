# NOTE: This implementation is correct but runs too long
# for inputs that are very large but still below 2*10^5.
# Need to make this solution faster




import math
number = [int(n) for n in input().strip()]

sub_sum = 0
pass_num = 0

# for each pass, group pass_num number of inputs together
while pass_num < len(number):
    pass_num += 1

    for i in range(0, pass_num):
        #print(i)
        #print([math.pow(10, i)*num for num in number[pass_num-i-1:len(number)-i]])
        sub_sum += sum([int(math.pow(10, i)*num) for num in number[pass_num-i-1:len(number)-i]])
        
print(int(sub_sum%(math.pow(10, 9)+7)))



