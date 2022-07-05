def longest_substring(string):

    char_set = set()
    result = 0
    l = 0

    for r in range(len(string)):
        while string[r] in char_set:
            char_set.remove(string[l])
            l += 1
        char_set.add(string[r])
        result = max(result, r-l+1)
    
    return result


print(longest_substring("abcabcbb"))
        

