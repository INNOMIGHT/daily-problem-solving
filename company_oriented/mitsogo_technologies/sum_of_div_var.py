def sum_of_div_var(low, high):

    div_variables = []
    for i in range(low, high+1):
        if ((i % 3 == 0) and (i % 5 == 0)):
            div_variables.append(i)

    return sum(div_variables)


print(sum_of_div_var(20, 50))
