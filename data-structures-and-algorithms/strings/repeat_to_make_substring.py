def repeat_x_times(string_one, string_two):

    repeat_counter = 0
    while len(string_one) <= len(string_two):
        if string_one == string_two:
            return repeat_counter
        string_one += string_one
        repeat_counter += 1
    pointer_one = 0
    pointer_two = len(string_two)

    while pointer_two != len(string_one):
        if string_one[pointer_one:pointer_two] == string_two:
            return repeat_counter
        pointer_one += 1
        pointer_two += 1

    return -1



print(repeat_x_times("abcd", "cdabcdab"))