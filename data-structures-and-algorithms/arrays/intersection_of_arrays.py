from collections import Counter

def intersection(arr1, arr2):
    c = Counter(arr1)
    print(c)
    output = []
    for n in arr2:
        if c[n]>0:
            print(c[n])
            output.append(n)
            c[n] -= 1
    return output
    


print(intersection([1,2,1, 2], [2,2]))