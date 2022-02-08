def group_anagrams(strs):

    word_dict = dict()

    for word in strs:
        sorted_word_list = sorted(word)
        sorted_word = "".join(sorted_word_list)

        if sorted_word not in word_dict:
            word_dict[sorted_word] = []
        
        word_dict[sorted_word].append(word)

    result = []
    for key, value in word_dict.items():
        result.append(value)

    return result
    
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))