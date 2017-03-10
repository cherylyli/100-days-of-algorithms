# Solved in ~5 min


#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    answer = 0
    dict_of_nums = {}
    for ind, val in enumerate(a):
        dict_of_nums[val] = ind
    for val in a:
        if val+k in dict_of_nums:
            answer += 1

    return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
