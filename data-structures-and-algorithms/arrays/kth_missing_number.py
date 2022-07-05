def kth_missing(arr, k):

    complete_arr = []
    start = arr[0]
    for i in range(start, arr[-1], 1):
        complete_arr.append(i)

    counter = 0
    i = 0
    j = 0
    result_end = arr[-1]
    result = 0
    result_exceeded = False
    while counter != k:
        if arr[i] != complete_arr[j]:
            result = complete_arr[j]
            j += 1
            counter += 1
        elif arr[i] == complete_arr[j]:
            i += 1
            j += 1
        if arr[i] == arr[-1]:
            result_end += 1
            counter += 1
            result_exceeded = True
    
    if result_exceeded:
        print(result_end)
    else:
        print(result)


    print(complete_arr)

print(kth_missing([1, 2, 4], 3))
