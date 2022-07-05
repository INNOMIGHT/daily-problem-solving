def who_is_going_home_early(n, k):
    array = [i for i in range(1,n+1)]
    a = array
    new_arr = []
    for _ in range(n//2):
        rotated_array = rotateArray(a, len(array), k)
        new_arr.append(rotated_array.pop(0))
        a = rotated_array
    return new_arr
    
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr


print(who_is_going_home_early(3, 4))