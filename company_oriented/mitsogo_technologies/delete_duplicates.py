from os import dup


def delete_duplicates(arr):

    freq = {}
    duplicates = []
    result = []
    for i in (arr):
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key, value in freq.items():
        if value > 1:
            duplicates.append(key)
        else:
            result.append(key)
    
    return arr


print(delete_duplicates([1, 2, 3, 4, 5, 4, 4]))
