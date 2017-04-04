# Not super efficient: keeps running into memory limit exceeded problem

# read from stdin
n, m = [int(i) for i in input().strip().split(" ")]

if m == 0:
    print(0)
change = [int(i) for i in input().strip().split(" ")]
change.sort()
min_c = change[0]
max_c = change[-1]

if min_c > n:
    print(0)

memo = {}

for i in range(min_c, change[-1]+1):
    new_changes = []
    # if i - some value in change is in memo
    for c in change:
        if i-c in memo:
            old_changes = memo[i-c]
            for coin_change in old_changes:
                coin_change = coin_change[:]
                if c >= coin_change[-1]:
                    coin_change.append(c)
                    new_changes.append(coin_change)

        if i == c:
            new_changes.append([c])
            
    memo[i] = new_changes
            
for i in range(change[-1]+1, n+1):
    new_changes = []
    # if i - some value in change is in memo
    for c in change:
        if i-c in memo:
            old_changes = memo[i-c]
            for coin_change in old_changes:
                coin_change = coin_change[:]
                if c >= coin_change[-1]:
                    coin_change.append(c)
                    new_changes.append(coin_change)

    memo[i] = new_changes
    if i-max_c in memo:
        del memo[i-max_c]

                    
print(len(memo[n]))