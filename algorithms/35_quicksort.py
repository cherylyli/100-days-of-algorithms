def swap(arr, i_0, i_1):
    """
    swap the i_0th and i_1th element in array arr 
    """
    temp = arr[i_0]
    arr[i_0] = arr[i_1]
    arr[i_1] = temp

def quicksort(a, start, end):
    """
    quicksort on a, return sorted array
    """
    # base case
    if end == start:
        return
    
    # let index of pivot be random
    pivot = a[end]
    
    small = start
    largerOrEqual = -1


    # loop through array, swap and pivot as necessary
    for i in range(start, end):
        if a[i] <= pivot:
            if largerOrEqual == -1:
                small += 1
            else:
                swap(arr, small, i)
                small += 1
                largerOrEqual = i
        else:
            if largerOrEqual == -1:
                largerOrEqual = i
            else:
                largerOrEqual += 1
                
    # swap the pivot to bewteen the less than and greater than parts
    swap(arr, small, end)
                
    # print statement for evaluation
    print(" ".join([str(num) for num in a]))
    
    # do partition on smaller half and on largerOrEqual half
    if small != start:
        quicksort(a, start, small-1)
    
    if largerOrEqual>0 and small != end:
        quicksort(a, small+1, end)
 
            
# parse input
n = int(input().strip())
arr = [int(i) for i in input().strip().split(" ")]
quicksort(arr, 0, n-1)
        
    