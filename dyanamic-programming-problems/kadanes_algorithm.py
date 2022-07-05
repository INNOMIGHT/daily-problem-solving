# maximum subarray
def kadanes_algo(arr):

    max_sum = 0
    curr_max = 0

    for i in range(len(arr)):
        curr_max = arr[i] + curr_max

        if curr_max > max_sum:
            max_sum = curr_max
        if curr_max < 0:
            curr_max = 0
    
    return max_sum


print(kadanes_algo([-2, 3, -1, 2]))