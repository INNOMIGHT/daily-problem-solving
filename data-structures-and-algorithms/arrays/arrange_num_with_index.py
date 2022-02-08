def rearrange(arr):
    result = []
    for i in range(len(arr)):
        if i in arr:
            result.append(i)
        else:
            result.append(-1)
    
    return result


print(rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]))