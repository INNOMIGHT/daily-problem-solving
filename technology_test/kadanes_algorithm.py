# maximum subarray algorithm by Kadane
def max_subarray(arr):
    if arr == []:
        return
    elif len(arr) == 1:
        return arr[0]
    curr_sum = arr[0]
    max_sum = arr[0]
    for num in range(1, arr): 
        if max_sum < curr_sum:
            max_sum = curr_sum
        curr_sum = max(arr[num]+curr_sum, curr_sum)

    return max_sum