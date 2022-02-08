def maximize_product(num):
    product = 1

    if num == 2 or num == 3:
        return num - 1
    
    else:
        while num > 4:
            product = product * 3
            num -= 3
    
    return num * product

# Using DP
    # dp = [1] * (num+1)
    # dp[0], dp[1], dp[2], dp[3], dp[4], dp[5], dp[6] = 0, 1, 1, 2, 4, 6, 9
    # for i in range(7, num+1):
    #     dp[i] = dp[i-3] * 3
    # return dp[num]


print(maximize_product(10))
