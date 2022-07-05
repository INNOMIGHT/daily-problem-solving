def find_palindromes(low, high):

    palindromes = []
    for i in range(low, high+1):
        str_i = str(i)
        if str_i == str_i[::-1]:
            palindromes.append(int(str_i))
    
    return palindromes


print(find_palindromes(10, 50))