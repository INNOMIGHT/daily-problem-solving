def swap_char(string, chr_1, chr_2):

    string = string.lower()
    char_list = list(string)
    for i in range(0, len(string)):
        if string[i] == chr_1:
            char_list[i] = chr_2
        elif string[i] == chr_2:
            char_list[i] = chr_1

    result = "".join(char_list)

    return result


print(swap_char("hello", "o", "l"))